import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 核心参数定义（根据题目给定） ----------------------
mu0 = 4 * np.pi * 1e-7  # 真空磁导率 (T·m/A)
R = 0.1  # 线圈半径 (m)，题目给定 R=10cm=0.1m
N0 = 400  # 线圈匝数，题目给定 N0=400
I = 0.4  # 励磁电流 (A)，题目给定 I=400mA=0.4A

# ---------------------- 实验数据整理（11个测量点） ----------------------
# 轴向距离 X (单位：m)，对应题目中的 10^-2 m（即cm）
x_experiment = np.array([-5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00, 4.00, 5.00]) * 1e-2
# 对应的实验测量磁感应强度 B (单位：μT)
b_experiment = np.array([735, 820, 895, 957, 998, 1010, 994, 948, 880, 804, 715])

# ---------------------- 理论曲线数据生成（平滑曲线，无标记点） ----------------------
# 生成密集的轴向距离点（-10cm 到 10cm），确保曲线平滑
x_theory = np.linspace(-0.1, 0.1, 100)  # 100个采样点，覆盖范围更广
# 理论公式：B(x) = (mu0 * N0 * I * R²) / [2 * (R² + x²)^(3/2)]
numerator = mu0 * N0 * I * R ** 2
denominator = 2 * (R ** 2 + x_theory ** 2) ** (3/2)
b_theory = (numerator / denominator) * 1e6  # 转换为 μT 单位（1T=1e6μT）

# ---------------------- 绘图设置 ----------------------
plt.rcParams['axes.unicode_minus'] = False    # 支持负号显示
fig, ax = plt.subplots(figsize=(10, 6))       # 画布大小

# ---------------------- 绘制曲线 ----------------------
# 实验值：红色实线 + 圆形标记（突出测量点），线宽2，标记大小6
ax.plot(x_experiment * 100, b_experiment, color='#E74C3C', linewidth=2, marker='o', 
        markersize=6, label='Measured B(μT)')
# 理论值：蓝色平滑曲线（无标记点），线宽2.5，强调理论趋势
ax.plot(x_theory * 100, b_theory, color="#2349F2", linewidth=2.5, linestyle='--', 
        label='Theoretical B(μT)')

# ---------------------- 图表美化与标注 ----------------------
# 标题：还原实验报告英文标题，加粗
ax.set_title('Magnetic Induction B vs Axial Distance X', fontsize=14, fontweight='bold', pad=20)
# 横坐标标签：单位转换为 cm（更直观），对应题目中的 10^-2 m
ax.set_xlabel('Axial X (cm)', fontsize=12, labelpad=10)
# 纵坐标标签：明确单位 μT
ax.set_ylabel('Magnetic Induction B (μT)', fontsize=12, labelpad=10)

# 坐标轴范围优化（匹配数据分布，使曲线居中）
ax.set_xlim(-6, 6)
ax.set_ylim(650, 1050)

# 刻度设置：横坐标每1cm一个刻度，纵坐标每50μT一个刻度
ax.set_xticks(np.arange(-6, 7, 1))
ax.set_yticks(np.arange(650, 1051, 50))

# 添加网格线（浅色虚线，提升可读性）
ax.grid(True, color='#F0F0F0', linestyle=':', linewidth=1)

# 图例：右上角位置，清晰区分两条曲线
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# 调整布局，避免标签截断
plt.tight_layout()

# ---------------------- 保存与显示 ----------------------
# 高分辨率保存（300dpi），支持插入实验报告
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')

# ---------------------- 验证信息输出（可选，用于核对理论值） ----------------------
center_b_theory = (mu0 * N0 * I) / (2 * R) * 1e6  # 中心处（x=0）理论值
print(f"线圈中心处（x=0）理论磁场强度：{center_b_theory:.1f} μT")
print(f"实验中心处磁场强度：{b_experiment[5]} μT")
print(f"中心处相对误差：{abs(b_experiment[5] - center_b_theory) / center_b_theory * 100:.1f}%")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 数据整理（严格对应用户提供的轴向测量数据） ----------------------
# 轴向距离 X (单位：cm)，按表格顺序完整提取31个实验点
x_data = [
    -10.00, -9.50, -9.00, -8.50, -8.00, -7.50, -7.00, -6.50, -6.00, -5.50, -5.00,
    -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 5.50, 6.00,
    6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50, 10.00
]
# 对应的磁感应强度 B (单位：μT)，与x_data一一对应
b_data = [
    877, 932, 986, 1042, 1098, 1152, 1202, 1244, 1284, 1316, 1348, 1388, 1407,
    1416, 1416, 1416, 1416, 1416, 1410, 1390, 1354, 1326, 1296, 1256, 1216, 1170,
    1120, 1066, 1008, 956, 898
]

# ---------------------- 绘图基础设置（全英文，无中文） ----------------------
plt.rcParams['axes.unicode_minus'] = False  # 支持负号显示
fig, ax = plt.subplots(figsize=(12, 6))     # 加宽画布以更好展示平台区

# ---------------------- 绘制实验曲线 ----------------------
# 实验值：指定蓝色#2253F4 + 圆形标记，线宽2.5，标记大小5（密集数据点适配）
ax.plot(x_data, b_data, color='#2253F4', linewidth=2.5, marker='o', 
        markersize=5, markerfacecolor='#2253F4', markeredgecolor='white', 
        markeredgewidth=0.5, label='Measured B')

# ---------------------- 关键标注（还原实验报告图表特征） ----------------------
max_b = max(b_data)
# 找到最大值对应的x范围（平台区：-2.00~2.00 cm）
max_x_range = [x for x, b in zip(x_data, b_data) if b == max_b]
max_x_str = f"{min(max_x_range):.2f}~{max(max_x_range):.2f} cm"
# 在最大值平台区标注，位置偏移避免遮挡
ax.text(0.0, max_b + 20, f'Max B={max_b} μT at X={max_x_str}', 
        fontsize=12, fontweight='bold', color='#E74C3C', ha='center')

# 标注均匀磁场平台区（用阴影强调）
ax.axvspan(-2.0, 2.0, alpha=0.1, color='#2253F4', label='Uniform Magnetic Field Region')

# ---------------------- 图表美化（全英文规范，匹配实验报告风格） ----------------------
# 标题：与实验报告一致的英文标题，加粗
ax.set_title('Magnetic Induction B vs Axial Distance X', fontsize=14, fontweight='bold', pad=20)
# 横坐标标签：明确单位(cm)，与实验报告一致
ax.set_xlabel('Axial Distance X (cm)', fontsize=12, labelpad=10)
# 纵坐标标签：明确单位(μT)，与实验报告一致
ax.set_ylabel('Magnetic Induction B (μT)', fontsize=12, labelpad=10)

# 坐标轴范围优化（覆盖数据并突出平台区）
ax.set_xlim(-12.0, 12.0)
ax.set_ylim(800, 1500)

# 刻度设置：横坐标每1cm一个刻度，纵坐标每50μT一个刻度
ax.set_xticks(np.arange(-12, 13, 1))
ax.set_yticks(np.arange(800, 1501, 50))

# 添加网格线（浅色虚线，提升数据可读性）
ax.grid(True, color='#F0F0F0', linestyle=':', linewidth=1)

# 图例（包含平台区标注，位置在右上角）
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# 调整布局，避免标签截断
plt.tight_layout()

# ---------------------- 保存与显示 ----------------------
# 高分辨率保存（300dpi），文件名贴合实验内容
plt.savefig('plot3.png', dpi=300, bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 数据整理（严格对应用户提供的径向测量数据） ----------------------
# 径向距离 Y (单位：cm)，共10个实验点
y_data = [-5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00, 4.00, 5.00]
# 对应的磁感应强度 B (单位：μT)
b_data = [1236, 1140, 1078, 1036, 1016, 1008, 1016, 1038, 1084, 1148, 1256]

# ---------------------- 绘图基础设置（全英文，无中文） ----------------------
plt.rcParams['axes.unicode_minus'] = False  # 支持负号显示
fig, ax = plt.subplots(figsize=(10, 6))     # 保持画布大小与前图一致

# ---------------------- 绘制实验曲线 ----------------------
# 实验值：深蓝色实线 + 圆形标记，线宽2.5，标记大小7（突出数据点）
ax.plot(y_data, b_data, color="#2253F4", linewidth=2.5, marker='o', 
        markersize=7, markerfacecolor='#2253F4', markeredgecolor='#2253F4', 
        label='Measured B')

# ---------------------- 图表美化（全英文规范，匹配实验报告风格） ----------------------
# 标题：与实验报告一致的英文标题，加粗
ax.set_title('Magnetic Induction B vs Radial Distance Y', fontsize=14, fontweight='bold', pad=20)
# 横坐标标签：明确单位(cm)，与实验报告一致
ax.set_xlabel('Radial Distance Y (cm)', fontsize=12, labelpad=10)
# 纵坐标标签：明确单位(μT)，与实验报告一致
ax.set_ylabel('Magnetic Induction B (μT)', fontsize=12, labelpad=10)

# 坐标轴范围优化（覆盖数据并留出余量，曲线居中）
ax.set_xlim(-6.0, 6.0)
ax.set_ylim(950, 1300)

# 刻度设置：横坐标每1cm一个刻度，纵坐标每50μT一个刻度
ax.set_xticks(np.arange(-6, 7, 1))
ax.set_yticks(np.arange(950, 1301, 50))

# 添加网格线（浅色虚线，提升数据可读性）
ax.grid(True, color='#F0F0F0', linestyle=':', linewidth=1)

# 图例（简洁英文标签，位置在右上角）
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# 调整布局，避免标签截断
plt.tight_layout()

# ---------------------- 保存与显示 ----------------------
# 高分辨率保存（300dpi），文件名贴合实验内容
plt.savefig('plot2.png', dpi=300, bbox_inches='tight')

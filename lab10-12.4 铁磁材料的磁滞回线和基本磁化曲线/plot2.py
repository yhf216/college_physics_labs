import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 核心数据 ----------------------
# X轴：磁场强度 H（单位：A/m）
H_b = [0, 734, 906, 1078, 1265, 1468, 1656, 1984, 2265, 2578, 2906]  # B-H曲线（含原点）
H_mu = [734, 906, 1078, 1265, 1468, 1656, 1984, 2265, 2578, 2906]     # μ-H曲线（不含原点）

# 左Y轴：磁感应强度 B（单位：T）
B = [0, 0.494, 0.651, 0.807, 0.963, 1.100, 1.217, 1.471, 1.588, 1.705, 1.862]

# 右Y轴：磁导率 μ（单位：10⁻⁴H/m）
mu = [6.734, 7.180, 7.484, 7.613, 7.491, 7.348, 7.413, 7.011, 6.615, 6.406]

# ---------------------- 绘图配置 ----------------------
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows中文支持（Mac/Linux替换为'Arial Unicode MS'）
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.rcParams['figure.dpi'] = 300  # 默认显示清晰度
plt.rcParams['lines.linewidth'] = 2.5  # 线条宽度

# 创建图形（宽12cm，高8cm）
fig, ax1 = plt.subplots(figsize=(12, 8))

# ---------------------- 左Y轴：基本磁化曲线（B-H）- 加深蓝色 ----------------------
color1 = '#0047AB'  # 加深蓝色（原#1E90FF优化为深蓝色）
line1 = ax1.plot(H_b, B, color=color1, marker='o', markersize=7,
                 markerfacecolor='#2C3E50', markeredgecolor='white', markeredgewidth=1.5,
                 label='基本磁化曲线（B-H）')

# 左Y轴配置
ax1.set_xlabel('磁场强度 H (A/m)', fontsize=14, fontweight='bold', labelpad=15)
ax1.set_ylabel('磁感应强度 B (T)', fontsize=14, fontweight='bold', color=color1, labelpad=15)
ax1.tick_params(axis='y', labelcolor=color1, labelsize=12, width=1.5, length=6)
ax1.set_xlim(0, max(H_b) * 1.05)
ax1.set_ylim(0, max(B) * 1.05)

# ---------------------- 右Y轴：磁导率变化曲线（μ-H）- 修复10⁻⁴显示 ----------------------
ax2 = ax1.twinx()
color2 = '#DC143C'  # 橙色保持不变
line2 = ax2.plot(H_mu, mu, color=color2, marker='s', markersize=7,
                 markerfacecolor='#B71C1C', markeredgecolor='white', markeredgewidth=1.5,
                 label='磁导率变化曲线（μ-H）')

# 右Y轴配置 - 修复10⁻⁴显示（使用LaTeX语法确保上标正常）
ax2.set_ylabel(r'磁导率 $\mu$ ($10^{-4}\ \text{H/m}$)', fontsize=14, fontweight='bold', color=color2, labelpad=15)
ax2.tick_params(axis='y', labelcolor=color2, labelsize=12, width=1.5, length=6)
ax2.set_ylim(min(mu) * 0.95, max(mu) * 1.05)

# ---------------------- 图形美化 ----------------------
ax1.grid(True, linestyle='--', alpha=0.5, linewidth=1, color='#CCCCCC')
# 合并图例
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, fontsize=12, loc='upper left', framealpha=0.95, shadow=True)

# 标题
ax1.set_title('基本磁化曲线与磁导率变化曲线',
              fontsize=16, fontweight='bold', pad=20)

# 调整布局
plt.tight_layout()

# ---------------------- 保存图片（不显示，仅保存） ----------------------
plt.savefig('plot2.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

# ---------------------- 数据统计输出（控制台）----------------------
print("双Y轴图像已保存，数据统计：")
print(f"1. 基本磁化曲线（B-H）：{len(H_b)} 组数据（含原点）")
print(f"   - H范围：{min(H_b)} ~ {max(H_b)} A/m")
print(f"   - B范围：{min(B)} ~ {max(B)} T")
print(f"2. 磁导率变化曲线（μ-H）：{len(H_mu)} 组数据")
print(f"   - H范围：{min(H_mu)} ~ {max(H_mu)} A/m")
print(f"   - μ范围：{min(mu):.3f} ~ {max(mu):.3f} ×10⁻⁴H/m")
print(f"3. 磁导率峰值：{max(mu):.3f} ×10⁻⁴H/m（对应H={H_mu[mu.index(max(mu))]} A/m）")
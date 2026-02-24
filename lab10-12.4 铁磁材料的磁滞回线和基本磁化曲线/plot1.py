import matplotlib.pyplot as plt
import numpy as np

# ---------------------- 完整30组H-B数据（直接嵌入，无需外部文件）----------------------
# 磁场强度 H（单位：A/m，第一列数据）
H = [
    1983.692308, 1594.153846, 1017.230769, 541.3846154, 0,
    -490.1538462, -865.3846154, -1153.846154, -1341.230769, -1528.615385,
    -1644, -1716, -1759.384615, -1874.769231, -2033.538462,
    -1644, -1254.461538, -865.3846154, -389.5384615, 0,
    504.4615385, 836.3076923, 1110.461538, 1369.846154, 1542.923077,
    1658.307692, 1716, 1745.076923, 1802.769231, 1918.153846
]

# 磁感应强度 B（单位：T，第二列数据，与H一一对应）
B = [
    1.348064516, 1.31016129, 1.234677419, 1.159032258, 1.033064516,
    0.869193548, 0.68016129, 0.478548387, 0.302096774, 0,
    -0.251935484, -0.718225806, -1.23483871, -1.297741935, -1.335645161,
    -1.297741935, -1.247419355, -1.196935484, -1.121451613, -1.033225806,
    -0.869354839, -0.705645161, -0.516612903, -0.277096774, 0,
    0.302419355, 0.692903226, 1.23483871, 1.28516129, 1.323064516
]

# ---------------------- 关键处理：使曲线闭合（首尾点相连）----------------------
H_closed = H + [H[0]]
B_closed = B + [B[0]]

# ---------------------- 筛选含0的特殊点（H=0 或 B=0）----------------------
special_H = []
special_B = []
common_H = []
common_B = []
for h, b in zip(H, B):
    if abs(h) < 1e-6 or abs(b) < 1e-6:
        special_H.append(h)
        special_B.append(b)
    else:
        common_H.append(h)
        common_B.append(b)

# ---------------------- 核心计算：剩磁、矫顽力、磁滞损耗 ----------------------
# 1. 剩磁（Br）：H=0时的磁感应强度（单位：T）
remanence = []  # 存储所有H=0对应的B值
for h, b in zip(special_H, special_B):
    if abs(h) < 1e-6:
        remanence.append(b)
Br_positive = max(remanence, key=abs)  # 正向剩磁（绝对值最大的正向B）
Br_negative = min(remanence, key=abs)  # 反向剩磁
Br_average = (abs(Br_positive) + abs(Br_negative)) / 2  # 平均剩磁

# 2. 矫顽力（Hc）：B=0时的磁场强度绝对值（单位：A/m）
coercivity = []  # 存储所有B=0对应的H绝对值
for h, b in zip(special_H, special_B):
    if abs(b) < 1e-6:
        coercivity.append(abs(h))
Hc_positive = coercivity[0]  # 正向矫顽力（B=0时的负H绝对值）
Hc_negative = coercivity[1]  # 反向矫顽力（B=0时的正H绝对值）
Hc_average = (Hc_positive + Hc_negative) / 2  # 平均矫顽力

# 3. 磁滞损耗：闭合曲线面积积分（单位：J/m³，物理意义：单位体积磁化一周的能量损耗）
# 采用梯形积分法，积分方向沿闭合曲线顺序，确保面积为正
hysteresis_loss = abs(np.trapz(B_closed, H_closed))  # abs确保损耗为正

# ---------------------- 绘图配置（无图例，保持其他优化）----------------------
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows中文支持（Mac/Linux替换为'Arial Unicode MS'）
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.rcParams['figure.dpi'] = 300  # 默认显示清晰度

fig, ax = plt.subplots(figsize=(12, 9))

# 1. 绘制闭合磁滞回线（蓝色实线，线宽2.5）
ax.plot(H_closed, B_closed, color='#1E90FF', linewidth=2.5, zorder=1)

# 2. 标注普通数据点（深蓝色实心点，尺寸60，白色细边框）
ax.scatter(common_H, common_B, color='#00008B', s=60, marker='o', 
           edgecolor='white', linewidth=1, zorder=2)

# 3. 标注特殊点（红色实心点，尺寸120，白色粗边框，突出显示）
ax.scatter(special_H, special_B, color='#DC143C', s=120, marker='o', 
           edgecolor='white', linewidth=2, zorder=3)

# ---------------------- 智能比例优化 ----------------------
x_min, x_max = min(H_closed), max(H_closed)
y_min, y_max = min(B_closed), max(B_closed)
x_margin = (x_max - x_min) * 0.1
y_margin = (y_max - y_min) * 0.1

ax.set_xlim(x_min - x_margin, x_max + x_margin)
ax.set_ylim(y_min - y_margin, y_max + y_margin)

# ---------------------- 图形美化与可读性增强 ----------------------
ax.set_xlabel('磁场强度 H (A/m)', fontsize=14, fontweight='bold', labelpad=15)
ax.set_ylabel('磁感应强度 B (T)', fontsize=14, fontweight='bold', labelpad=15)
ax.set_title('铁磁材料H-B磁滞回线', 
             fontsize=16, fontweight='bold', pad=20)

# 浅灰色虚线网格，不遮挡数据点和曲线
ax.grid(True, linestyle='--', alpha=0.5, linewidth=1, color='#EEEEEE')

# 坐标轴刻度优化（字体放大，刻度线加粗）
ax.tick_params(axis='both', which='major', labelsize=12, width=1.5, length=6)
ax.tick_params(axis='both', which='minor', width=1, length=3)

# 调整布局，防止标签被截断
plt.tight_layout()

# ---------------------- 保存与显示 ----------------------
# 保存300dpi高分辨率图片（无图例，画面更简洁）
plt.savefig('plot1.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

# ---------------------- 详细结果输出（控制台）----------------------
print("="*60)
print("铁磁材料磁滞回线关键参数计算结果")
print("="*60)
print(f"1. 剩磁（Br）：")
print(f"   - 正向剩磁：{Br_positive:.6f} T")
print(f"   - 反向剩磁：{Br_negative:.6f} T")
print(f"   - 平均剩磁：{Br_average:.6f} T")
print("-"*60)
print(f"2. 矫顽力（Hc）：")
print(f"   - 正向矫顽力（B=0时）：{Hc_positive:.2f} A/m")
print(f"   - 反向矫顽力（B=0时）：{Hc_negative:.2f} A/m")
print(f"   - 平均矫顽力：{Hc_average:.2f} A/m")
print("-"*60)
print(f"3. 磁滞损耗（单位体积）：{hysteresis_loss:.2f} J/m³")
print(f"   （物理意义：单位体积铁磁材料每磁化一个周期消耗的能量）")
print("="*60)
print(f"数据点统计：总{len(H)}个 | 普通点{len(common_H)}个 | 特殊点{len(special_H)}个")
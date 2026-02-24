import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# -------------------------- 1. 配置中文显示（解决乱码问题）--------------------------
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统推荐字体（黑体）
# 若为Mac系统，替换为：plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 若为Linux系统，替换为：plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常问题
plt.rcParams['text.usetex'] = False  # 禁用LaTeX渲染（避免兼容性问题）
plt.rcParams['mathtext.fontset'] = 'cm'  # 保留基础数学符号兼容性

# -------------------------- 2. 整理实验数据 --------------------------
# 温度 t (单位：℃)
t = np.array([24.0, 30.3, 35.0, 39.8, 45.0, 50.3, 55.2, 60.0, 65.3, 70.8])
# 电阻 Rx (单位：10^-3 Ω，数据直接对应该量级)
Rx = np.array([4.595, 4.710, 4.795, 4.885, 4.978, 5.070, 5.160, 5.242, 5.330, 5.420])

# -------------------------- 3. 线性拟合与R²计算 --------------------------
# 拟合方程：R_x = slope·t + intercept（slope单位：10^-3 Ω/℃；intercept单位：10^-3 Ω）
slope, intercept, r_value, p_value, std_err = stats.linregress(t, Rx)
R_squared = r_value ** 2  # 决定系数R²

# 生成拟合线数据（使拟合线更平滑）
t_fit = np.linspace(t.min() - 1, t.max() + 1, 100)
Rx_fit = slope * t_fit + intercept  # 拟合线电阻值（单位：10^-3 Ω）

# -------------------------- 4. 绘制Rx-t曲线 --------------------------
plt.figure(figsize=(10, 6))  # 画布大小

# 绘制实验数据散点图
plt.scatter(t, Rx, color='#E74C3C', s=60, alpha=0.8, label='实验数据', edgecolors='black', linewidth=0.5)

# 绘制线性拟合线（统一为你指定的 $10^{-3}\\,\\Omega$ 格式）
plt.plot(t_fit, Rx_fit, color='#3498DB', linewidth=2.5, linestyle='--', 
         label=f'线性拟合: $R_x = ({slope:.6f}t + {intercept:.3f}) \\times 10^{-3}\\,\\Omega$')

# 设置坐标轴标签（ylabel沿用你指定的格式，xlabel保持一致）
plt.xlabel('温度 t (℃)', fontsize=13, fontweight='bold')
plt.ylabel('电阻 $R_x$ ($10^{-3}\\,\\Omega$)', fontsize=13, fontweight='bold')  # 完全按你的要求保留

# 图表标题
plt.title('$R_x$-$t$曲线', fontsize=15, fontweight='bold', pad=20)

# 图例（左上角）
plt.legend(loc='upper left', fontsize=11, framealpha=0.9)

# 网格线
plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.8)

# R²值（右下角+黑色边框）
plt.text(0.75, 0.05, f'决定系数 $R^2 = {R_squared:.6f}$', 
         transform=plt.gca().transAxes,
         fontsize=12, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=1.2, alpha=0.9))

# 刻度字体大小
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 调整布局（避免标签被截断）
plt.tight_layout()

# 显示图像
plt.show()

# -------------------------- 5. 输出拟合结果（格式统一，控制台兼容显示）--------------------------
print(f"线性拟合方程：R_x = ({slope:.6f}t + {intercept:.3f}) × 10^-3 Ω")
print(f"决定系数 R² = {R_squared:.6f}")
print(f"拟合斜率：{slope:.6f} (10^-3 Ω/℃)")
print(f"拟合截距：{intercept:.3f} (10^-3 Ω)")
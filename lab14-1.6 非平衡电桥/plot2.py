# 导入所需库
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# ====================== 1. 整理实验数据 ======================
# Temperature (℃)
t = np.array([23.0, 28.9, 34.2, 39.1, 44.1, 50.2, 56.3, 62.3])
# Resistance of Cu50 (Ω)
R = np.array([55.30, 56.55, 57.70, 58.74, 59.83, 61.20, 62.47, 63.78])

# ====================== 2. 线性拟合（避免特殊字符） ======================
fit_results = linregress(t, R)
slope = fit_results.slope          # Slope (Ω/℃)
intercept = fit_results.intercept  # Intercept (Ω)
r_squared = fit_results.rvalue **2  # R-squared (fit goodness)

# 用ASCII星号(*)替代乘号×，避免编码乱码
fit_equation = f"R = {slope:.4f} * t + {intercept:.4f}"

# ====================== 3. 输出拟合结果（用R^2替代R²，避免编码报错） ======================
print("===== Fitting Results =====")
print(f"Fitting Equation: {fit_equation}")
print(f"R^2 (Coefficient of Determination): {r_squared:.6f}")  # 用^表示平方，纯ASCII

# ====================== 4. 绘制曲线 ======================
t_fit = np.linspace(min(t), max(t), 100)
R_fit = slope * t_fit + intercept

plt.figure(figsize=(9, 6))
# 原始数据点
plt.scatter(t, R, color='blue', s=60, label='Experimental Data', zorder=3)
# 拟合曲线
plt.plot(t_fit, R_fit, color='blue', linewidth=2, label='Fitting Curve', zorder=2)

# 标注拟合方程和R^2（全ASCII，无特殊字符）
annotation = f"{fit_equation}\nR^2 = {r_squared:.6f}"
plt.text(0.05, 0.95, annotation, transform=plt.gca().transAxes, 
         fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ====================== 5. 图表标注（全英文+纯ASCII） ======================
plt.xlabel('Temperature t (℃)', fontsize=12)
plt.ylabel('Resistance R (Ω)', fontsize=12)
plt.title('Resistance-Temperature Characteristic Curve of Cu50', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, zorder=1)
plt.legend(loc='lower right', fontsize=11)

# ====================== 6. 保存图片 ======================
plt.savefig('plot2.png', dpi=300, bbox_inches='tight')
# 无plt.show()，直接保存
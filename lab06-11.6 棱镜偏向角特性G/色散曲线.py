import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 设置中文显示（关键修正）
plt.rcParams["font.family"] = ["SimHei"]  # 支持中文的字体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 1. 数据准备（提取波长和折射率，统一单位）
# 波长单位：nm -> m（1nm=1e-9m），折射率直接取用
wavelength_nm = np.array([404.7, 435.8, 546.0, 577.1])  # 波长（nm）
wavelength_m = wavelength_nm * 1e-9  # 转换为米
n = np.array([1.7078, 1.6990, 1.6765, 1.6728])  # 折射率

# 2. 定义柯西色散公式：n(λ) = a + b/λ² + c/λ⁴
def cauchy(lam, a, b, c):
    return a + b / (lam**2) + c / (lam**4)

# 3. 曲线拟合（使用最小二乘法）
popt, pcov = curve_fit(cauchy, wavelength_m, n)
a, b, c = popt  # 拟合得到的参数

# 4. 输出拟合参数
print("柯西色散公式拟合参数：")
print(f"a = {a:.6f}")
print(f"b = {b:.2e} m²")  # 单位：m²（因λ单位为m）
print(f"c = {c:.2e} m⁴")  # 单位：m⁴

# 5. 绘制色散曲线
plt.figure(figsize=(8, 5))

# 绘制原始数据点
plt.scatter(wavelength_nm, n, color='red', marker='o', label='实验数据')

# 绘制拟合曲线（用密集波长点生成曲线）
lam_fit = np.linspace(min(wavelength_nm), max(wavelength_nm), 100)  # 拟合区间
lam_fit_m = lam_fit * 1e-9  # 转换为米
n_fit = cauchy(lam_fit_m, a, b, c)
plt.plot(lam_fit, n_fit, color='blue', linestyle='-', label='柯西公式拟合曲线')

# 图表设置
plt.xlabel('波长 (nm)', fontsize=12)
plt.ylabel('折射率 n', fontsize=12)
plt.title('n-λ 关系曲线', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
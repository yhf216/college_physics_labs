# 导入绘图库
import matplotlib.pyplot as plt

# ====================== 1. 整理数据 ======================
# Temperature t (℃)
t = [23.0, 28.9, 34.2, 39.1, 44.1, 50.2, 56.3, 62.3]
# Unbalanced voltage U (mV)
U = [30.5, 37.9, 44.5, 50.4, 56.4, 63.7, 70.4, 77.1]

# ====================== 2. 绘图设置 ======================
# 移除中文字体配置（无需处理中文，避免显示异常）
plt.figure(figsize=(8, 5))  # Canvas size: 8 inches (width) × 5 inches (height)

# 绘制曲线（散点+折线，清晰展示数据点和趋势）
plt.plot(t, U, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6, label='U-t Curve')

# ====================== 3. 图表标注（全英文） ======================
plt.xlabel('Temperature t (℃)', fontsize=12)  # X-axis label
plt.ylabel('Unbalanced Voltage U (mV)', fontsize=12)  # Y-axis label
plt.title('Curve of Unbalanced Voltage vs Temperature', fontsize=14, fontweight='bold')  # Title
plt.grid(True, alpha=0.3)  # Show grid (low transparency for readability)
plt.legend(loc='best')  # Show legend (auto find best position)

# ====================== 4. 保存图片 ======================
# Save as plot1.png, 300 dpi for high clarity, tight layout to avoid label truncation
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')

# No plt.show() - directly save the image to local directory
import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.ticker import MaxNLocator

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_experiment(data_x, data_y, labels, title, x_label, y_label, 
                    figsize=(10, 10), marker='o', linestyle='-', 
                    linewidth=2, markersize=8, grid=True, 
                    save_path=None, show=True):
    """
    绘制实验数据折线图
    
    参数:
    data_x: x轴数据
    data_y: y轴数据列表，每个元素是一条线的数据
    labels: 每条线的标签列表
    title: 图表标题
    x_label: x轴标签
    y_label: y轴标签
    figsize: 图表大小
    marker: 数据点标记样式
    linestyle: 线条样式
    linewidth: 线条宽度
    markersize: 标记大小
    grid: 是否显示网格
    save_path: 保存图片路径，None则不保存
    show: 是否显示图表
    """
    plt.figure(figsize=figsize)
    
    # 绘制多条线
    for y, label in zip(data_y, labels):
        plt.plot(data_x, y, marker=marker, linestyle=linestyle, 
                 linewidth=linewidth, markersize=markersize, label=label)
    
    # 设置标题和标签
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    
    # 设置网格
    if grid:
        plt.grid(True, linestyle='--', alpha=0.7)
    
    # 设置图例
    if labels:
        plt.legend(fontsize=10)
    
    # 设置坐标轴刻度为整数（如果适用）
    if all(isinstance(x, (int, np.integer)) for x in data_x):
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # 调整布局
    plt.tight_layout()
    
    # 保存图片
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        # 使用OpenCV读取并重新保存（如果需要）
        img = cv2.imread(save_path)
        if img is not None:
            cv2.imwrite(save_path, img)
    

def main():
    # 1. 改装5mA量程的电流表并校准数据
    current_standard = [1.00, 2.00, 3.00, 4.00, 5.00]  # I准/mA
    current_measured = [0.21, 0.41, 0.61, 0.80, 0.98]  # I测/mA
    current_modified = [1.05, 2.05, 3.05, 4.00, 4.90]  # I改/mA
    current_error = [0.05, 0.05, 0.05, 0.00, -0.10]    # ΔI/mA
    
    # 绘制电流表校准曲线（补充labels参数，单条线用单元素列表）
    plot_experiment(
        data_x=current_standard,
        data_y=[current_modified],
        labels=['改装后电流'],  # 补充标签
        title='改装5mA量程的电流表校准曲线',
        x_label='标准电流I准 (mA)',
        y_label='电流值 (mA)',
        marker='o',  # 单条线无需列表
        save_path='5mA.png'
    )
    
    # 新增：电流表误差ΔI与标准电流I准的关系曲线
    plot_experiment(
        data_x=current_standard,
        data_y=[current_error],
        labels=['电流误差ΔI'],
        title='改装5mA量程电流表的误差曲线',
        x_label='标准电流I准 (mA)',
        y_label='电流误差ΔI (mA)',
        marker='o',
        save_path='5mA_error.png',
        figsize=(10,6)
    )

    # 2. 改装5V量程的电压表并校准数据
    voltage_standard = [1.00, 2.00, 3.00, 4.00, 5.00]  # V准/V
    voltage_current = [0.20, 0.40, 0.59, 0.78, 0.98]   # I测/mA
    voltage_modified = [1.00, 2.00, 2.95, 3.90, 4.90]  # V改/V
    voltage_error = [0.00, 0.00, -0.05, -0.10, -0.10]  # ΔV/V
    
    # 绘制电压表校准曲线（补充labels参数）
    plot_experiment(
        data_x=voltage_standard,
        data_y=[voltage_modified],
        labels=['改装后电压'],  # 补充标签
        title='改装5V量程的电压表校准曲线',
        x_label='标准电压V准 (V)',
        y_label='电压值(V)',
        marker='o',  # 单条线无需列表
        save_path='5V.png'
    )

    # 新增：电压表误差ΔV与标准电压V准的关系曲线
    plot_experiment(
        data_x=voltage_standard,
        data_y=[voltage_error],
        labels=['电压误差ΔV'],
        title='改装5V量程电压表的误差曲线',
        x_label='标准电压V准 (V)',
        y_label='电压误差ΔV (V)',
        marker='o',
        save_path='5V_error.png',
        figsize=(10,6)
    )
    
    # 3. 改装欧姆表数据
    resistance = [0, 100, 200, 300, 400, 500, 600, 700, 
                 800, 900, 1000, 2000, 3000, 5000, 10000, 30000]  # 电阻箱R/Ω
    current_ohmmeter = [1.00, 0.76, 0.60, 0.51, 0.43, 0.38, 0.34, 0.30,
                      0.28, 0.26, 0.23, 0.14, 0.10, 0.06, 0.04, 0.02]  # 表头电流I/mA
    
    # 绘制欧姆表曲线
    plot_experiment(
        data_x=resistance,
        data_y=[current_ohmmeter],
        labels=['表头电流'],
        title='改装欧姆表刻度对应关系',
        x_label='电阻箱阻值R (Ω)',
        y_label='表头电流I (mA)',
        marker='o',
        save_path='R.png'
    )

    # 4. 改装欧姆表数据（x轴取lg10处理）
    resistance_safe = resistance[1:]  
    current_ohmmeter_safe = current_ohmmeter[1:] 
    log_resistance = np.log10(resistance_safe)  # 对阻值取lg10
    
    # 绘制x轴取lg10后的欧姆表曲线
    plot_experiment(
        data_x=log_resistance,
        data_y=[current_ohmmeter_safe],
        labels=['表头电流'],
        title='改装欧姆表刻度对应关系',
        x_label='电阻箱阻值lgR(lgΩ)',  # x轴标签更新为对数处理后的说明
        y_label='表头电流I (mA)',
        marker='o',
        save_path='R_log.png'  # 保存为新文件，避免覆盖原图表
    )

if __name__ == "__main__":
    main()
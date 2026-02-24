# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator
from typing import Optional


# 中文显示配置（适配Windows终端）
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False


def plot_delta_s_delta_t(excel_path: str,
                         sheet_name: str = "Sheet1",
                         delta_s_col: str = "delta_s_cm",  # Excel中Δs列名（纯英文）
                         delta_t_col: str = "delta_t_ns",  # Excel中Δt'列名（纯英文）
                         title: str = "Δs与Δt'关系折线图",
                         x_label: str = "Δs (cm)",  # 用delta_s替代Δs，避免编码问题
                         y_label: str = "Δt' (ns)",  # 用delta_t'替代Δt'
                         figsize: tuple = (10, 6),
                         marker: str = 'o',
                         linestyle: str = '-',
                         linewidth: float = 2,
                         markersize: float = 8,
                         grid: bool = True,
                         save_path: Optional[str] = "ts.png",
                         show: bool = True,
                         sort_ascending: bool = True,
                         c_true: float = 2.998e8) -> None:  # 光速准确值（m/s）
    """
    适配说明：
    1. Excel列名要求：Δs列→"delta_s_cm"，Δt'列→"delta_t_ns"（纯英文，无特殊符号）
    2. 用"delta_s"替代"Δs"、"R^2"替代"R²"，避免GBK编码冲突
    3. 新增功能：考虑Δs重复点的权重（重复次数越多，权重越大）
    """
    # -------------------------- 1. 读取Excel数据 --------------------------
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet_name, engine="openpyxl")
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel文件不存在：{excel_path}\n请检查路径（例：D:/实验数据.xlsx）")
    except ValueError as e:
        raise ValueError(f"读取工作表失败：{str(e)}\n请检查工作表名'{sheet_name}'是否正确")
    
    # 检查必要列
    required_cols = [delta_s_col, delta_t_col]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(
            f"Excel缺少列：{missing_cols}\n"
            f"请修改Excel列名：\n"
            f"- 原Δs列 → 改名为 'delta_s_cm'\n"
            f"- 原Δt'列 → 改名为 'delta_t_ns'"
        )
    
    # 提取数据（去空值）
    delta_s = df[delta_s_col].dropna().values  # 自变量：delta_s（cm）
    delta_t = df[delta_t_col].dropna().values  # 因变量：delta_t'（ns）
    if len(delta_s) != len(delta_t):
        raise ValueError(f"delta_s数据长度（{len(delta_s)}）与delta_t'数据长度（{len(delta_t)}）不匹配")


    # -------------------------- 2. 按delta_s升序排序 --------------------------
    paired_data = sorted(zip(delta_s, delta_t), key=lambda x: x[0], reverse=not sort_ascending)
    delta_s_sorted = np.array([p[0] for p in paired_data])  # 排序后delta_s（x轴）
    delta_t_sorted = np.array([p[1] for p in paired_data])  # 排序后delta_t'（y轴）


    # -------------------------- 新增：计算权重（重复点权重更高） --------------------------
    # 统计每个delta_s的出现次数作为权重（重复次数越多，权重越大）
    unique_s, counts = np.unique(delta_s_sorted, return_counts=True)
    weight_dict = {s: cnt for s, cnt in zip(unique_s, counts)}
    weights = np.array([weight_dict[s] for s in delta_s_sorted])  # 生成与数据点对应的权重数组
    # 移除emoji，避免GBK编码错误
    print(f"数据点权重统计：重复的Δs值将被赋予更高权重")
    for s, cnt in zip(unique_s, counts):
        if cnt > 1:
            print(f"   - Δs={s}cm 出现{cnt}次，权重为{cnt}")


    # -------------------------- 3. 加权线性拟合+R^2+不确定度计算 --------------------------
    # 3.1 加权线性拟合：delta_t' = k×delta_s + b（加入权重参数w）
    k, b = np.polyfit(delta_s_sorted, delta_t_sorted, deg=1, w=weights, cov=False)
    k, b = round(k, 6), round(b, 4)
    
    # 拟合值与残差
    delta_t_fit = k * delta_s_sorted + b
    residuals = delta_t_sorted - delta_t_fit


    # 3.2 R^2拟合优度（用R^2替代R²，避免编码问题）
    delta_t_mean = np.mean(delta_t_sorted)
    ss_tot = np.sum((delta_t_sorted - delta_t_mean) **2)
    ss_res = np.sum(residuals** 2)
    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0.0
    r2 = round(r2, 6)


    # 3.3 拟合参数不确定度（使用加权拟合的协方差）
    coeffs, cov = np.polyfit(delta_s_sorted, delta_t_sorted, deg=1, w=weights, cov=True)
    sigma_k = np.sqrt(cov[0, 0])  # 斜率标准误差
    sigma_b = np.sqrt(cov[1, 1])  # 截距标准误差
    sigma_k, sigma_b = round(sigma_k, 8), round(sigma_b, 6)


    # 3.4 光速计算（物理关系：delta_t' = delta_s/c → c = delta_s/delta_t' = 1/k × 1e7）
    c_meas = (1 / k) * 1e7  # 测量光速（m/s）
    sigma_c = (sigma_k / (k ** 2)) * 1e7  # 光速标准误差
    rel_uncertainty = (sigma_c / c_meas) * 100 if c_meas != 0 else 0.0  # 相对不确定度
    rel_deviation = ((c_meas - c_true) / c_true) * 100  # 与准确值偏差
    
    # 保留有效数字
    c_meas = round(c_meas, 2)
    sigma_c = round(sigma_c, 2)
    rel_uncertainty = round(rel_uncertainty, 4)
    rel_deviation = round(rel_deviation, 4)


    # -------------------------- 4. 终端输出（纯文本，无GBK编码冲突） --------------------------
    print("=" * 85)
    print("                 delta_s-delta_t' 加权线性拟合与光速分析结果（考虑重复点权重）")
    print("=" * 85)
    print(f"1. 加权线性拟合方程：delta_t' = {k} × delta_s + {b}")
    print(f"   - 斜率k：{k} ns/cm（物理意义：每1cm光程差对应的时间差）")
    print(f"   - 截距b：{b} ns（理论应为0，非零值反映系统误差）")
    print(f"2. 拟合优度R^2：{r2}（≥0.99为优秀线性关系，越接近1越好）")  # R^2替代R²
    print("-" * 85)
    print(f"3. 拟合参数不确定度：")
    print(f"   - 斜率标准误差σ_k：{sigma_k} ns/cm（越小，斜率越稳定）")
    print(f"   - 截距标准误差σ_b：{sigma_b} ns（越小，截距越稳定）")
    print("-" * 85)
    print(f"4. 光速计算结果（准确值c_true = {c_true:.2e} m/s）：")
    print(f"   - 测量值c_meas：{c_meas:.2e} m/s")
    print(f"   - 测量标准误差σ_c：{sigma_c:.2e} m/s")
    print(f"   - 相对不确定度：{rel_uncertainty}%（精度指标，越小越好）")
    print(f"   - 与准确值的相对偏差：{rel_deviation}%（准确度指标，绝对值越小越好）")
    print("=" * 85)


    # -------------------------- 5. 绘图（无特殊符号，避免编码问题） --------------------------
    plt.figure(figsize=figsize)
    
    # 绘制原始数据连线
    plt.plot(delta_s_sorted, delta_t_sorted,
             marker=marker, linestyle=linestyle,
             linewidth=linewidth, markersize=markersize,
             color='#1f77b4', label='原始数据点', zorder=3)
    
    # 绘制加权线性拟合线（图例用R^2）
    plt.plot(delta_s_sorted, delta_t_fit,
             linestyle='--', linewidth=linewidth+1,
             color='#ff7f0e', label=f'加权拟合线（Δt\'={k}×Δs+{b}，R^2={r2}）', zorder=4)
    
    # 图表样式
    plt.title(title, fontsize=14, pad=20, fontweight='bold')
    plt.xlabel(x_label, fontsize=12, fontweight='bold')
    plt.ylabel(y_label, fontsize=12, fontweight='bold')
    plt.grid(grid, linestyle='--', alpha=0.6, color='gray', zorder=1)
    plt.legend(fontsize=10, loc='upper left', frameon=True, shadow=True)
    
    # 坐标轴整数刻度
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    
    # 保存与显示
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        # 移除emoji，避免GBK编码错误
        print(f"\n图表已保存至：{save_path}")
    if show:
        plt.show()


# -------------------------- 代码调用入口 --------------------------
if __name__ == "__main__":
    # 1. 修改为你的Excel实际路径（相对路径/绝对路径）
    EXCEL_FILE_PATH = "实验数据.xlsx"
    
    # 2. 调用函数
    plot_delta_s_delta_t(
        excel_path=EXCEL_FILE_PATH,
        sheet_name="Sheet1",  # 若工作表名不是Sheet1，需修改
        save_path="ts2.png"
    )
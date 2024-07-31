import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

def analyze_K(file_path, stock_num=1001, output_image_path='K_graph.png'):
    # 读取数据
    df = pd.read_excel(file_path)
    stock_code = int(stock_num)
    df = df[df['股票代码'] == stock_code]
    if df.empty:
        print(f"未找到股票代码为 {stock_code} 的数据。")
        return  # 退出函数，不再执行绘图代码
    # 确保数据按日期排序
    df.sort_values('日期', inplace=True)

    # 将'日期'列转换为pandas的datetime类型
    df['日期'] = pd.to_datetime(df['日期'])

    ohlc_data = df[['日期', '开盘价', '最高价', '最低价', '收盘价']].copy()

    # 解决FutureWarning，使用.to_numpy()替代.to_pydatetime()
    ohlc_data['日期数值'] = mdates.date2num(ohlc_data['日期'].to_numpy())

    fig, ax = plt.subplots(figsize=(12, 6))

    # 绘制K线图
    candlestick_ohlc(ax, ohlc_data[['日期数值', '开盘价', '最高价', '最低价', '收盘价']].values, width=0.6,
                     colorup='green', colordown='red', alpha=0.8)

    # 设置标题
    ax.set_title(f'Stock {stock_code} Candlestick chart')

    # 格式化x轴日期显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.savefig(output_image_path, dpi=300, format='png')
    # 关闭图表以避免内存泄漏
    plt.close()


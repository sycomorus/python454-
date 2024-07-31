import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np

def analyze_candle_stick(file_path, stock_num=1001, output_image_path='candle_stick.png'):
   
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

    # 计算移动平均线
    df['MA5'] = df['收盘价'].rolling(window=5).mean()
    df['MA10'] = df['收盘价'].rolling(window=10).mean()
    df['MA30'] = df['收盘价'].rolling(window=30).mean()

    # 准备绘制蜡烛图的数据
    ohlc_data = df[['日期', '开盘价', '最高价', '最低价', '收盘价']].copy()

    # 将日期转换为数值格式
    ohlc_data['日期数值'] = mdates.date2num(np.array(ohlc_data['日期']))

    # 绘制蜡烛图
    fig, ax = plt.subplots(figsize=(20, 10))

    # 绘制5天、10天、30天移动平均线
    ax.plot(df['日期'], df['MA5'], color='green', label='MA5')
    ax.plot(df['日期'], df['MA10'], color='orange', label='MA10')
    ax.plot(df['日期'], df['MA30'], color='red', label='MA30')

    # 绘制蜡烛图
    candlestick_ohlc(ax, ohlc_data[['日期数值', '开盘价', '最高价', '最低价', '收盘价']].values, width=0.6,
                     colorup='green', colordown='red', alpha=0.8)

    # 设置图例和标题
    ax.legend()
    ax.set_title(f'Stock {stock_code} - OHLC with 5, 10, and 30 Days Moving Averages')

    # 格式化x轴日期显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    # 显示图表
    plt.tight_layout()  # Adjust the layout to fit all labels
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # Close the plot to avoid memory leaks


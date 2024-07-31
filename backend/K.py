import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc


def read_df_stock():
    num = int(input("请输入股票代码: "))
    return num


def show_pictures(num):
    # 读取数据
    df = pd.read_excel('金融-精简化股市数据分析(2).xlsx')
    df = df[df['股票代码'] == num]
    if df.empty:
        print(f"未找到股票代码为 {num} 的数据。")
        return  # 退出函数，不再执行绘图代码
    # 确保数据按日期排序
    df.sort_values('日期', inplace=True)

    # 将'日期'列转换为pandas的datetime类型
    df['日期'] = pd.to_datetime(df['日期'])

    ohlc_data = df[['日期', '开盘价', '最高价', '最低价', '收盘价']].copy()

    ohlc_data['日期数值'] = mdates.date2num(ohlc_data['日期'].dt.to_pydatetime())

    fig, ax = plt.subplots(figsize=(12, 6))

    candlestick_ohlc(ax, ohlc_data[['日期数值', '开盘价', '最高价', '最低价', '收盘价']].values, width=0.6,
                     colorup='green', colordown='red', alpha=0.8)

    # 设置图例和标题
    ax.legend()
    ax.set_title(f'Stock {num} Candlestick chart')

    # 格式化x轴日期显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    plt.savefig('basic_assignment_e.png', dpi=300, format='png')
    # 显示图表
    plt.show()


show_pictures(read_df_stock())

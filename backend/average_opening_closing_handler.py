import pandas as pd
import matplotlib.pyplot as plt

def analyze_opening_closing(file_path, output_image_path='Average_opening_closing.png'):
    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    # 数据处理：计算平均开盘价和收盘价
    avg_open = df.groupby('股票代码')['开盘价'].mean()
    avg_close = df.groupby('股票代码')['收盘价'].mean()

    # 合并成一个 DataFrame
    avg_prices = pd.DataFrame({'Average opening price': avg_open, 'Average closing price': avg_close})

    # 绘制开盘价和收盘价平均条形图
    plt.figure(figsize=(10, 6))
    avg_prices.plot(kind='bar', color=['blue', 'red'])
    plt.title('Average opening and closing prices of stocks')
    plt.xlabel('Stock code')
    plt.ylabel('price')
    plt.legend()
    plt.xticks(rotation=45)  # 旋转标签，便于阅读
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

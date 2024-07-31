import pandas as pd
import matplotlib.pyplot as plt

def analyze_max_price(file_path, output_image_path='max_price.png'):
    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    max_prices = df.groupby('股票代码')['最高价'].max().reset_index()

    # 绘制条形图
    plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.bar(max_prices['股票代码'], max_prices['最高价'], color='blue')  # 绘制条形图

    # 设置标题和标签
    plt.title('The highest price reached by each stock')
    plt.xlabel('Stock code')
    plt.ylabel('max price')

    # 显示X轴的标签
    plt.xticks(rotation=45)  # 旋转标签，便于阅读

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # 关闭绘图，避免内存泄漏
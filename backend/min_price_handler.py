import pandas as pd
import matplotlib.pyplot as plt

def analyze_min_price(file_path, output_image_path='min_price.png'):

    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    min_prices = df.groupby('股票代码')['最低价'].min().reset_index()

    # 绘制条形图
    plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.bar(min_prices['股票代码'], min_prices['最低价'], color='green')  # 绘制条形图

    # 设置标题和标签
    plt.title('The lowest price reached by each stock')
    plt.xlabel('Stoke code')
    plt.ylabel('min price')

    # 显示X轴的标签
    plt.xticks(rotation=45)  # 旋转标签，便于阅读

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # 关闭绘图，避免内存泄漏
import pandas as pd
import matplotlib.pyplot as plt

def analyze_volume_of_business(file_path, output_image_path='volume_of_business.png'):
    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    # 4. 绘制其他图表的代码类似，只需更改数据集和图表类型即可
    # 例如，绘制总成交量条形图
    total_volume = df.groupby('股票代码')['交易量'].sum()
    total_volume.plot(kind='bar', color='green', label='total volume')
    plt.title('Total trading volume of stocks')
    plt.xlabel('Stock code')
    plt.ylabel('volume of business')
    n = 5
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # 关闭绘图，避免内存泄漏


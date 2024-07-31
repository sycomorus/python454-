import pandas as pd
import matplotlib.pyplot as plt

def analyze_turnover(file_path, output_image_path='Average_turnover.png'):
    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    # 按股票代码分组，并计算每组的日平均换手率
    average_turnover = df.groupby('股票代码')['换手率'].mean().reset_index()

    # 绘制条形图
    plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.bar(average_turnover['股票代码'], average_turnover['换手率'], color='blue')  # 绘制条形图

    # 设置标题和标签
    plt.title('Average turnover rate of each stock')
    plt.xlabel('Stock code')
    plt.ylabel('Average turnover')

    # 显示X轴的标签
    plt.xticks(rotation=45)  # 旋转标签，便于阅读

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # 关闭绘图，避免内存泄漏

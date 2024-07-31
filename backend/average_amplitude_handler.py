import pandas as pd
import matplotlib.pyplot as plt

def analyze_amplitude(file_path, output_image_path='Average_amplitude.png'):
    # 1. 读取Excel数据
    df = pd.read_excel(file_path)

    # 按股票代码分组，并计算每组的日平均振幅
    average_amplitude = df.groupby('股票代码')['振幅'].mean().reset_index()

    # 绘制散点图
    plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.scatter(average_amplitude['股票代码'], average_amplitude['振幅'], color='purple', alpha=0.5)  # 绘制散点图

    # 设置标题和标签
    plt.title('Average amplitude of each stock')
    plt.xlabel('Stock code')
    plt.ylabel('Average amplitude')

    # 显示X轴的标签
    plt.xticks(rotation=45)  # 旋转标签，便于阅读

    # 显示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

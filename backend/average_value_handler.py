import pandas as pd
import matplotlib.pyplot as plt

# this is for assignment c

# 1. 读取Excel数据
def analyze_average_value(file_path, stock_num=1001, output_image_path='stock_chart.png'):
    # 1. Read Excel data
    df = pd.read_excel(file_path)
    stock_code=int(stock_num)
    df = df[df['股票代码'] == stock_code]

    df = df.sort_values('日期')

    # 计算5日、10日和30日移动平均值
    df['MA5'] = df['收盘价'].rolling(window=5).mean()
    df['MA10'] = df['收盘价'].rolling(window=10).mean()
    df['MA30'] = df['收盘价'].rolling(window=30).mean()

    # 绘制收盘价折线图
    plt.figure(figsize=(14, 7))
    plt.plot(df['日期'], df['收盘价'], label='closing price', color='blue')

    # 绘制均线
    plt.plot(df['日期'], df['MA5'], label='5 days average', color='red', linestyle='--')
    plt.plot(df['日期'], df['MA10'], label='10 days average', color='green', linestyle='-.')
    plt.plot(df['日期'], df['MA30'], label='30 days average', color='black', linestyle='-')

    # 标注金叉和死亡交叉
    # 金叉：当日的5日均线高于10日均线，而昨日的5日均线低于10日均线
    golden_cross = df[(df['MA5'] > df['MA10']) & (df['MA5'].shift(1) < df['MA10'].shift(1))]
    # 死亡交叉：当日的5日均线低于10日均线，而昨日的5日均线高于10日均线
    death_cross = df[(df['MA5'] < df['MA10']) & (df['MA5'].shift(1) > df['MA10'].shift(1))]

    # 绘制金叉和死亡交叉点
    # for idx, row in golden_cross.iterrows():
    #     plt.scatter(row['日期'], row['收盘价'], color='yellow', label='kdj')
    #
    # for idx, row in death_cross.iterrows():
    #     plt.scatter(row['日期'], row['收盘价'], color='purple', label='Death crossing')

    if not golden_cross.empty:
        plt.scatter(golden_cross['日期'], golden_cross['收盘价'], color='green', label='kdj', marker='^')

    # 绘制死亡交叉点
    if not death_cross.empty:
        plt.scatter(death_cross['日期'], death_cross['收盘价'], color='yellow', label='Death crossing', marker='v')

    # 添加图例、标题和轴标签
    plt.title('Closing price and moving average of stocks')
    # plt.legend(['closing price', '5 days average', '10 days average', '30 days average', 'kdj', 'Death crossing'])
    plt.legend(loc='best')
    plt.xlabel('Date')
    plt.ylabel('price')

    # 旋转日期标签，避免重叠
    plt.xticks(rotation=45)

    # 展示图表
    plt.tight_layout()  # 调整布局以适应所有标签
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # 关闭绘图，避免内存泄漏















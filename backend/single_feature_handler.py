import pandas as pd
import matplotlib.pyplot as plt

def analyze_trading_volume(file_path, stock_code,output_image_path='trading_volume.png'):
    df=pd.read_excel(file_path)
    df=df[df['股票代码']==int(stock_code)]
    plt.figure(figsize=(14, 7))
    plt.bar(df['日期'], df['交易量'], color='blue')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Trading Volume Over Time')
    plt.tight_layout()
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

def analyze_price_change_rate(file_path, stock_code,output_image_path='price_change_rate.png'):
    df=pd.read_excel(file_path)
    df=df[df['股票代码']==int(stock_code)]
    plt.figure(figsize=(14, 7))
    plt.plot(df['日期'], df['涨跌幅'], color='green')
    plt.xlabel('Date')
    plt.ylabel('Price Change Rate')
    plt.title('Price Change Rate Over Time')
    plt.tight_layout()
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

def analyze_single_amplitude(file_path, stock_code,output_image_path='amplitude.png'):
    df=pd.read_excel(file_path)
    df=df[df['股票代码']==int(stock_code)]
    plt.figure(figsize=(14, 7))
    plt.plot(df['日期'], df['振幅'], color='red')
    plt.xlabel('Date')
    plt.ylabel('Amplitude')
    plt.title('Amplitude Over Time')
    plt.tight_layout()
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

def analyze_turnover_rate(file_path, stock_code,output_image_path='turnover_rate.png'):
    df=pd.read_excel(file_path)
    df=df[df['股票代码']==int(stock_code)]
    plt.figure(figsize=(14, 7))
    plt.plot(df['日期'], df['换手率'], color='orange')
    plt.xlabel('Date')
    plt.ylabel('Turnover Rate')
    plt.title('Turnover Rate Over Time')
    plt.tight_layout()
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()

import pandas as pd
import matplotlib.pyplot as plt


def analyze_composite_rise_and_fall(file_path, output_image_path='Compositerise and fall.png'):
    # 1. Read Excel data
    df = pd.read_excel(file_path)

    # Calculate the opening price at the beginning of the year and the closing price at the end of the year for each stock
    first_day_prices = df.groupby('股票代码')['开盘价'].first()  # Opening price at the beginning of the year
    last_day_prices = df.groupby('股票代码')['收盘价'].last()   # Closing price at the end of the year

    # Calculate the compound rise and fall
    compound_change = ((last_day_prices / first_day_prices) - 1) * 100  # Convert to percentage

    # Draw a bar chart
    plt.figure(figsize=(10, 6))  # Set the size of the chart
    positive_changes = compound_change[compound_change > 0]
    # compound_change.plot(kind='bar', color='orange')  # Draw a bar chart
    plt.bar(positive_changes.index, positive_changes, color='orange')

    # Set the title and labels
    plt.title('Composite annual rise and fall of various stocks')
    plt.xlabel('Stock code')
    plt.ylabel('Composite rise and fall (%)')

    # If the rise and fall is negative, display different colors on the bar chart
    negative_changes = compound_change[compound_change < 0]
    plt.bar(negative_changes.index, negative_changes, color='red')

    # Display the labels on the X-axis
    plt.xticks(rotation=45)  # Rotate the labels for easy reading

    # plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

    # Display the chart
    plt.tight_layout()  # Adjust the layout to fit all labels
    plt.savefig(output_image_path, dpi=300, format='png')
    plt.close()  # Close the plot to avoid memory leaks
   

import os
from datetime import datetime

from backend.average_amplitude_handler import analyze_amplitude
from backend.average_opening_closing_handler import analyze_opening_closing
from backend.average_turnover_handler import analyze_turnover
from backend.volume_of_business_handler import analyze_volume_of_business
from backend.max_price_handler import analyze_max_price
from backend.min_price_handler import analyze_min_price
from backend.composite_rise_and_fall_handler import analyze_composite_rise_and_fall
from backend.average_value_handler import analyze_average_value
from backend.single_feature_handler import (
    analyze_trading_volume,
    analyze_price_change_rate,
    analyze_single_amplitude,
    analyze_turnover_rate
)
from backend.candlestick_handler import analyze_candle_stick
from backend.K_handler import analyze_K

class FileHandler:
    def __init__(self, user):
        file = f"analysis/{user}"
        # self.output_directory = os.path.join(os.path.dirname(__file__), '..', file)
        self.output_directory = os.path.abspath(file)
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def analyze_file(self,file_path, analysis_type,stock_code=-1):
        if analysis_type == "amplitude":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_amplitude(file_path,output_image_path)
        elif analysis_type == "opening_closing":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_opening_closing(file_path,output_image_path)
        elif analysis_type == "turnover":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_turnover(file_path,output_image_path)
        elif analysis_type == "volume_of_business":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_volume_of_business(file_path,output_image_path)
        elif analysis_type == "max_price":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_max_price(file_path,output_image_path)
        elif analysis_type == "min_price":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_min_price(file_path,output_image_path)
        elif analysis_type == "composite_rise_and_fall":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_composite_rise_and_fall(file_path,output_image_path)
        
        elif analysis_type == "average_value":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_average_value(file_path,stock_code,output_image_path)
        elif analysis_type == "single_trading_volume":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_trading_volume(file_path,stock_code,output_image_path)
        elif analysis_type == "single_price_change_rate":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_price_change_rate(file_path,stock_code,output_image_path)
        elif analysis_type == "single_amplitude":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_single_amplitude(file_path,stock_code,output_image_path)
        elif analysis_type == "single_turnover_rate":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_turnover_rate(file_path,stock_code,output_image_path)
        elif analysis_type == "candlestick":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_candle_stick(file_path,stock_code,output_image_path)
        elif analysis_type == "K":
            output_image_path =os.path.join(self.output_directory,self.gen_file_name(analysis_type,stock_code))
            analyze_K(file_path,stock_code,output_image_path)
            
        return output_image_path

    def gen_file_name(self, analysis_type, stock_code):
        current_time = datetime.now()
        current_time = current_time.strftime("%Y-%m-%d %H %M %S")
        if stock_code != -1:
            file_name = f"{current_time}_{stock_code}_{analysis_type}.png"
        else:
            file_name = f"{current_time}_{analysis_type}.png"
        return file_name


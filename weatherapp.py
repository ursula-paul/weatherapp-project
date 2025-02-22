
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                            QLineEdit,QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self )
        self.temperature_label = QLabel("70F", self)
        self. emoji_label = QLabel("",self)
        self. description_label = QLabel("Sunny", self)
        self.initUI()
        
        
    def initUI(self):
        self.setWindowsTitle("Weather App")
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        
        self.city_label.setObjectName("city_label")
        self.city_label.setObjectName("city_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label_label.setObjectName("emoji_label")
        self.description_label.setObjectName("descrription_label")
        
        self.setStyleSheet("""
                        QLabel, QPushButton{
                            font-family:calibri;
                        }
                        QLabel#city_label{
                            font-size: 40px;
                            font-style:italic;
                            
                        }
                        QLineEdit#city_input{
                            font-size:40px
                        }
                        QPushButton#get_weather_button{
                            font-size:30px
                            font-weight:bold;
                        }
                        QLabel#temprature_label{
                            font-size:75px;
                        }
                        QLabel#emoji_label{
                            font-size: 100px;
                            font-family:segoe UI emoji;
                        }
                        QLabel#description_Label{
                            font-size: 50px;
                        }
                        """)
        
        
        
#if __name__ == "__main__":
    #super().__init__()
    
if __name__ == "__main__":
    app= QApplication(sys.argv)
    Weather_app = WeatherApp()
    Weather_app.show()
    sys.exit(app.exec_())
    
    

    
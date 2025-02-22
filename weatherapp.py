
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
        
        
#if __name__ == "__main__":
    #super().__init__()
    
if __name__ == "__main__":
    app= QApplication(sys.argv)
    Weather_app = WeatherApp()
    Weather_app.show()
    sys.exit(app.exec_())
    
    

    
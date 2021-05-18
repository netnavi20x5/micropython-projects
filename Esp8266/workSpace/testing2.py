from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
#i2c = I2C(-1, scl=Pin(4), sda=Pin(5))

# ESP8266 Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))
i2c = I2C(scl=Pin(4), sda=Pin(5))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('I am Awesome!', 0, 0)
oled.text('line1!', 0, 10)
oled.text('line2', 0, 20)
oled.text('line3', 0, 30)
oled.text('line4', 0, 40)
oled.text('line5', 0, 50)
oled.text('kill me!', 0, 60)
        
oled.show()



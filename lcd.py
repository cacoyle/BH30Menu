#!/usr/bin/python
import lcddriver

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("12345678901234567890", 1)
lcd.lcd_display_string("12345678901234567890", 2)
lcd.lcd_display_string("12345678901234567890", 3)
lcd.lcd_display_string("12345678901234567890", 4)

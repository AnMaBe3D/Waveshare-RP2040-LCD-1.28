# Simple program to show Pictures (BMP) on the Display
# Firmware: adafruit-circuitpython-raspberry_pi_pico-de_DE-7.3.3.uf2

# Modules and libraries
import board
import displayio
import busio
import pwmio
import time
from gc9a01 import GC9A01

# Variables
# Pins
pin_SDA = board.GP6
pin_SDL = board.GP7
pin_cs = board.GP9
pin_dc = board.GP8
pin_clk = board.GP10
pin_mosi = board.GP11
pin_reset = board.GP12
pin_backlight = board.GP25
pin_vBat = board.A3 

# Setup display
displayio.release_displays()
spi = busio.SPI(pin_clk, MOSI=pin_mosi)
display_bus = displayio.FourWire(spi, command=pin_dc, chip_select=pin_cs, reset=pin_reset)
display = GC9A01(display_bus, width=240, height=240, brightness=1)
led = pwmio.PWMOut(pin_backlight, frequency=5000, duty_cycle=40000) # max 65535

# Read files
bitmap0 = displayio.OnDiskBitmap("/0.bmp")
bitmap1 = displayio.OnDiskBitmap("/1.bmp")
#bitmap2 = displayio.OnDiskBitmap("/2.bmp")
#bitmap3 = displayio.OnDiskBitmap("/3.bmp")
#bitmap4 = displayio.OnDiskBitmap("/4.bmp")

group = displayio.Group()
display.show(group)

# Slideshow
while True:
    tile_grid = displayio.TileGrid(bitmap0, pixel_shader=bitmap0.pixel_shader)
    group.append(tile_grid)
    time.sleep(10)
    tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap1.pixel_shader)
    group.append(tile_grid)
    time.sleep(10)
#     tile_grid = displayio.TileGrid(bitmap2, pixel_shader=bitmap.pixel_shader)
#     group.pop()
#     group.append(tile_grid)
#     sleep(0.1)
#     tile_grid = displayio.TileGrid(bitmap3, pixel_shader=bitmap.pixel_shader)
#     group.pop()
#     group.append(tile_grid)
#     sleep(0.1)
#     tile_grid = displayio.TileGrid(bitmap4, pixel_shader=bitmap.pixel_shader)
#     group.pop()
#     group.append(tile_grid)
#     sleep(2)

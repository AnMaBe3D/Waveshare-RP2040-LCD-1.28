#I2C_SDA = 6
#I2C_SDL = 7

#DC = 8
#CS = 9
#SCK = 10
#MOSI = 11
#RST = 12

#BL = 25

#Vbat_Pin = 29

# modules and libraries
import board
import displayio
import busio
import time
from gc9a01 import GC9A01

# variables
pin_cs = board.GP9
pin_dc = board.GP8
pin_clk = board.GP10
pin_mosi = board.GP11
pin_reset = board.GP12

# setup display
displayio.release_displays()

spi = busio.SPI(pin_clk, MOSI=pin_mosi)

display_bus = displayio.FourWire(spi, command=pin_dc, chip_select=pin_cs, reset=pin_reset)

display = GC9A01(display_bus, width=240, height=240)

bitmap0 = displayio.OnDiskBitmap("/0.bmp")
#bitmap1 = displayio.OnDiskBitmap("/1.bmp")
#bitmap2 = displayio.OnDiskBitmap("/2.bmp")
#bitmap3 = displayio.OnDiskBitmap("/3.bmp")
#bitmap4 = displayio.OnDiskBitmap("/4.bmp")
group = displayio.Group()
display.show(group)

while True:
    tile_grid = displayio.TileGrid(bitmap0, pixel_shader=bitmap0.pixel_shader)
    group.append(tile_grid)
#    sleep(1)
#     tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap.pixel_shader)
#     group.append(tile_grid)
#     sleep(2)
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

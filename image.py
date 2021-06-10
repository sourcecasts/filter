import random
from PIL import Image, ImageDraw
import win32gui
import win32api


# цветной фильтр
def rgb_scale(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    context = win32gui.GetDC(0) 
    for x in range(source.size[0]):
     for y in range(source.size[1]):
         r, g, b = source.getpixel((x, y))
         gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
         wt = win32api.RGB(r, g, b)
         win32gui.SetPixel(context, x + 200, y + 200, wt)


# черно-белый фильтр
def white_black(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    context = win32gui.GetDC(0) 
    wt = win32api.RGB(255, 255, 255)
    wz = win32api.RGB(0, 0, 0)

    separator = 255 / brightness / 2 * 3
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            total = r + g + b

            if total > separator:
            	win32gui.SetPixel(context, x + 200, y + 200, wt)
            else:
                win32gui.SetPixel(context, x + 200, y + 200, wz)

# оттенки серого
def gray_scale(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    context = win32gui.GetDC(0) 
    for x in range(source.size[0]):
     for y in range(source.size[1]):
         r, g, b = source.getpixel((x, y))
         gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
         wt = win32api.RGB(gray, gray, gray)
         win32gui.SetPixel(context, x + 200, y + 200, wt)





rgb_scale("C:/Users/Root/Desktop/review.jpg", "C:/Users/Root/Desktop/result.jpg")
#gray_scale("C:/Users/Root/Desktop/review.jpg", "C:/Users/Root/Desktop/result.jpg")
#white_black("C:/Users/Root/Desktop/review.jpg", "C:/Users/Root/Desktop/result.jpg", 1.5)

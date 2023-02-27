# -------------------------
# ------- GIF MAKER -------
# -------------------------

import os
import time
from moviepy.editor import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print('--------------------------------------')
print('----- SPI DISPLAY GIF MAKER, 2023 ----')
print('--------------------------------------\n')

print('[-]  Please enter the input filename (include extention & no spaces in name):  ')

input_file = input('')
input_file = input_file.replace(' ', '')

clear()
print('[-]  Please enter an output filename:  ')
# Location in same directory as this script.

output_file = input('')
output_file = output_file.replace(' ', '')
if ('.gif' not in output_file):
    output_file += '.gif'

clear()
print('[-]  Enter the max width and height for the')
print('     output file (x,y formate):  ')

res = input('')
res = res.replace(' ', '')
res = res.replace('(', '')
res = res.replace(')', '')
res = res.replace('X', 'x')
if (',' in res):
    res = res.split(',')
else:
    res = res.split('x')

max_width = int(res[0])
max_height = int(res[1])

if ((max_width > 199) or (max_height > 199)):
    clear()
    print('[!]  Resolution of width or height greater that 200 pixels  ')
    print('     may result in far lower frame-rate!  \n')

    time.sleep(4)
else:
    clear()

print('[-]  Please enter a start-time. (ie. 0:05):  ')

start_time = input('')
start_time = start_time.replace(' ', '')

clear()
print('[-]  Please enter an end-time. (ie. 0:13):  ')

end_time = input('')
end_time = end_time.replace(' ', '')

start_time = start_time.split(":")
end_time = end_time.split(":")

start_min = start_time[0]
start_sec = start_time[1]
start_sec = start_sec.replace("00", "0")
start_sec = start_sec.replace("01", "1")
start_sec = start_sec.replace("02", "2")
start_sec = start_sec.replace("03", "3")
start_sec = start_sec.replace("04", "4")
start_sec = start_sec.replace("05", "5")
start_sec = start_sec.replace("06", "6")
start_sec = start_sec.replace("07", "7")
start_sec = start_sec.replace("08", "8")
start_sec = start_sec.replace("09", "9")
start_min = int(start_min)
start_sec = int(start_sec)
start_total_sec = ((start_min * 60) + start_sec)

end_min = end_time[0]
end_sec = end_time[1]
end_sec = end_sec.replace("00", "0")
end_sec = end_sec.replace("01", "1")
end_sec = end_sec.replace("02", "2")
end_sec = end_sec.replace("03", "3")
end_sec = end_sec.replace("04", "4")
end_sec = end_sec.replace("05", "5")
end_sec = end_sec.replace("06", "6")
end_sec = end_sec.replace("07", "7")
end_sec = end_sec.replace("08", "8")
end_sec = end_sec.replace("09", "9")
end_min = int(end_min)
end_sec = int(end_sec)
end_total_sec = ((end_min * 60) + end_sec)

difference = (end_total_sec - start_total_sec)

if (difference > 5):
    clear()
    print('[!]  A duration of greater than 5 seconds might need to')
    print('     be loaded from an SD card to fit.  \n')

    time.sleep(4)
else:
    clear()

print('[-]  Loading...  \n')

# Location in same directory as this script.
try:
    video = (VideoFileClip(input_file).subclip((start_min, start_sec), (end_min, end_sec)))
except:
    print('[!]  ERROR loading file!  Make sure the file is in the  ')
    print('     same directory as this script.  \n')
    time.sleep(4)
    exit()

if (max_width > max_height):
    video = video.resize(height = max_height)
    video_width = video.w

    if (video_width > max_width):
        video_difference = (video_width - max_width)
        left_crop = (video_difference / 2)
        right_crop = (video_width - left_crop)
        video = video.crop(x1 = left_crop, x2 = right_crop)
else:
    video_width = video.w
    video_height = video.h
    if (video_width > video_height):
        video = video.resize(height = max_height)
        video_width = video.w

        if (video_width > max_width):
            video_difference = (video_width - max_width)
            left_crop = (video_difference / 2)
            right_crop = (video_width - left_crop)
            video = video.crop(x1 = left_crop, x2 = right_crop)
    else:
        video = video.resize(width = max_width)
        video_height = video.h

        if (video_height > max_height):
            video_difference = (video_height - max_height)
            top_crop = (video_difference / 2)
            bottom_crop = (video_height - top_crop)
            video = video.crop(y1 = top_crop, y2 = bottom_crop)

video.write_gif(filename=output_file, fps=6, program='ffmpeg', fuzz=50)

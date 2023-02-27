# SPI DISPLAY GIF MAKER

This is a very simple GIF generator used to generate GIFs that can run in gifio on Circuit Python (currently 8.1.0 Beta).  This script alone is designed to run on a comupter with the moviepy library, NOT on Circuit Python hardware.

Sidenote - this was made on a Unix based machine, sorry in advanced if it loads weird on Windows.

Make sure the movie file is in the same directory as this script.

![Alt Text]( https://raw.githubusercontent.com/MichaelLacock/Gif_Maker/main/screenshots/1.png)

![Alt Text]( https://github.com/MichaelLacock/Gif_Maker/main/screenshots/2.png)

NOTE: The greater the resolution is, the more taxing it is to load the bitmap TileGrid in DisplayIO, resulting in far lower frame rates.

Here is a stable example of a Gif running on a 160x128 SPI display.

![Alt Text]( https://github.com/MichaelLacock/Gif_Maker/blob/main/screenshots/example.gif?raw=true
)

*** Example code for Circuit Python will be released soon, along side the release of my Display Plus Feather-Wing and Pico-Pal. Stay tuned!

Prototype Delight / Michael Lacock, 2023

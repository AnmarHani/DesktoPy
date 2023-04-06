# [DesktoPY](https://pypi.org/project/desktopy/)
## Description:
A Library For Building Desktop Applications and Interfaces that is built on top of tkinter, customtkinter, and other libraries associated.

## Getting Started:
You can install the library simply by writing:

``pip install desktopy``

Now, make a file, in our case ``main.py``:
```py
from desktopy import elements


```

<hr>
To build the application, just write:

``pyinstaller <your_main_file>.py``

(pyinstaller should be installed automatically with the DesktoPy package)

On completion, you can find your executable file inside 

``dist/<your_main_file>/<your_main_file>.exe``


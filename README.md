# Cowabunga Lite Py

The Python rewrite of Cowabunga Lite.

## Running the Program
Requirements:
- PySide6
- pymobiledevice3
- PyInstaller (for compiling an executable)

*Detailed install guide to go here later*

Note: It is highly recommended to use a virtual environment:
```
python -m venv env # only needed once
source env/bin/activate
pip install -r requirements.txt # only needed once
python main_app.py
```

## Building
To compile `mainwindow.ui` for Python, run the following command:
`pyside6-uic mainwindow.ui -o ui_mainwindow.py`

To compile the resources file for Python, run the following command:
`pyside6-rcc resources.qrc -o resources_rc.py`

The application itself can be compiled by running `compile.py`.

## Credits
- [Avangelista](https://github.com/Avangelista) and [Cowabunga Lite Windows](https://github.com/Avangelista/CowabungaLiteWindows) for the GUI.
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) for resoring and device algorithms.
- [PySide6](https://doc.qt.io/qtforpython-6/) for the GUI library.

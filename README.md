# Cowabunga Lite Py

The Python rewrite of Cowabunga Lite.

## Building
Requirements:
- PySide6
- pymobiledevice3
- cstruct

To compile `mainwindow.ui` for Python, run the following command:
`pyside6-uic mainwindow.ui -o ui_mainwindow.py`

To compile the resources file for Python, run the following command:
`pyside6-rcc resources.qrc -o resources_rc.py`

## Credits
- [Avangelista](https://github.com/Avangelista) and [Cowabunga Lite Windows](https://github.com/Avangelista/CowabungaLiteWindows) for the GUI.
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) for resoring and device algorithms.
- [PySide6](https://doc.qt.io/qtforpython-6/) for the GUI library.
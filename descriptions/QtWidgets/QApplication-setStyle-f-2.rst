.. sip:method-description::
    :status: todo
    :pysig: 7e0c1d20198d2d22b30ccc5863327cae
    :realsig: (const QString&)
    :digest: be39c9b0bab41c6d5d049e5379dbda67

Requests a :sip:ref:`~PyQt6.QtWidgets.QStyle` object for *style* from the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory`.

The string must be one of the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory.keys`, typically one of "windows", "windowsvista", "fusion", or "macos". Style names are case insensitive.

Returns ``nullptr`` if an unknown *style* is passed, otherwise the :sip:ref:`~PyQt6.QtWidgets.QStyle` object returned is set as the application's GUI style.

**Warning:** To ensure that the application's style is set correctly, it is best to call this function before the :sip:ref:`~PyQt6.QtWidgets.QApplication` constructor, if possible.

.. sip:method-description::
    :status: todo
    :pysig: 8e4fcb2cd4c5ca0e83aed7bbb3b5b54d
    :realsig: (const QString&)
    :digest: 2471c18eed131b605fb4e5603a5fb444

This is an overloaded function.

Requests a :sip:ref:`~PyQt6.QtWidgets.QStyle` object for *style* from the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory`.

The string must be one of the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory.keys`, typically one of "windows", "windowsvista", "fusion", or "macos". Style names are case insensitive.

Returns ``nullptr`` if an unknown *style* is passed, otherwise the :sip:ref:`~PyQt6.QtWidgets.QStyle` object returned is set as the application's GUI style.

**Warning:** To ensure that the application's style is set correctly, it is best to call this function before the :sip:ref:`~PyQt6.QtWidgets.QApplication` constructor, if possible.

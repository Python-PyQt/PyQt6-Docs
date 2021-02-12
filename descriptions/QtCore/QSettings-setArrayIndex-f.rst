.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d9cb8a984c5c2b78c77b4208832a01f2

Sets the current array index to *i*. Calls to functions such as :sip:ref:`~PyQt6.QtCore.QSettings.setValue`, :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.remove`, and :sip:ref:`~PyQt6.QtCore.QSettings.contains` will operate on the array entry at that index.

You must call :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray` or :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray` before you can call this function.

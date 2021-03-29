.. sip:method-description::
    :status: todo
    :pysig: 09e8d0bc807269e8f794180b11d99fbd
    :realsig: (const QFont&,const char*)
    :digest: 67a30a79768da188175ec682d97fed73

Changes the default application font to *font*. If *className* is passed, the change applies only to classes that inherit *className* (as reported by :sip:ref:`~PyQt6.QtCore.QObject.inherits`).

On application start-up, the default font depends on the window system. It can vary depending on both the window system version and the locale. This function lets you override the default font; but overriding may be a bad idea because, for example, some locales need extra large fonts to support their special characters.

**Warning:** Do not use this function in conjunction with `Qt Style Sheets <https://doc.qt.io/qt-6/stylesheet.html>`_. The font of an application can be customized using the "font" style sheet property. To set a bold font for all QPushButtons, set the application :sip:ref:`~PyQt6.QtWidgets.QApplication.styleSheet` as "\ :sip:ref:`~PyQt6.QtWidgets.QPushButton` { font: bold }"

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.font`, fontMetrics(), :sip:ref:`~PyQt6.QtWidgets.QWidget.setFont`.

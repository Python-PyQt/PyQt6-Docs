.. sip:method-description::
    :status: todo
    :pysig: de1ae28c667b917111c9f2c0958b4010
    :realsig: (const QPalette&,const char*)
    :digest: 1789373464b5308b4aa0c12f9a423565

Changes the application palette to *palette*.

If *className* is passed, the change applies only to widgets that inherit *className* (as reported by :sip:ref:`~PyQt6.QtCore.QObject.inherits`). If *className* is left 0, the change affects all widgets, thus overriding any previously set class specific palettes.

The palette may be changed according to the current GUI style in :sip:ref:`~PyQt6.QtWidgets.QStyle.polish`.

**Warning:** Do not use this function in conjunction with `Qt Style Sheets <https://doc.qt.io/qt-6/stylesheet.html>`_. When using style sheets, the palette of a widget can be customized using the "color", "background-color", "selection-color", "selection-background-color" and "alternate-background-color".

**Note:** Some styles do not use the palette for all drawing, for instance, if they make use of native theme engines. This is the case for the Windows Vista and macOS styles.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setPalette`, :sip:ref:`~PyQt6.QtWidgets.QApplication.palette`, :sip:ref:`~PyQt6.QtWidgets.QStyle.polish`.

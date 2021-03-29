.. sip:method-description::
    :status: todo
    :pysig: 0a35f1dec14ff0afb9c18ee980269a1b
    :realsig: (const QString&,int,int,bool)
    :digest: bf73a4659d3cb6765c2c29fb26aeb187

Constructs a font object with the specified *family*, *pointSize*, *weight* and *italic* settings.

If *pointSize* is zero or negative, the point size of the font is set to a system-dependent default value. Generally, this is 12 points.

The *family* name may optionally also include a foundry name, e.g. "Helvetica [Cronyx]". If the *family* is available from more than one foundry and the foundry isn't specified, an arbitrary foundry is chosen. If the family isn't available a family will be set using the `font matching <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ algorithm.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.Weight.Weight`, :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.setPointSize`, :sip:ref:`~PyQt6.QtGui.QFont.setWeight`, :sip:ref:`~PyQt6.QtGui.QFont.setItalic`, :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.font`.

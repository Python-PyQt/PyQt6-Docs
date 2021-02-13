.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: (const QFont&)
    :digest: 6cfe95f57e58721c9fb2c3f5ba4cfc93

Constructs a font metrics object for *font*.

The font metrics will be compatible with the paintdevice used to create *font*.

The font metrics object holds the information for the font that is passed in the constructor at the time it is created, and is not updated if the font's attributes are changed later.

Use :sip:ref:`~PyQt6.QtGui.QFontMetricsF`\ (const `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ &, :sip:ref:`~PyQt6.QtGui.QPaintDevice` \*) to get the font metrics that are compatible with a certain paint device.

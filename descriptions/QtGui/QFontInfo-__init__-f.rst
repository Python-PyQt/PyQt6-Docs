.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: (const QFont&)
    :digest: 7265a98a79fbcf90deecc7ea3aa60ebd

Constructs a font info object for *font*.

The font must be screen-compatible, i.e. a font you use when drawing text in :sip:ref:`~PyQt6.QtWidgets.QWidget` or :sip:ref:`~PyQt6.QtGui.QPixmap`, not :sip:ref:`~PyQt6.QtGui.QPicture` or :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`.

The font info object holds the information for the font that is passed in the constructor at the time it is created, and is not updated if the font's attributes are changed later.

Use :sip:ref:`~PyQt6.QtGui.QPainter.fontInfo` to get the font info when painting. This will give correct results also when painting on paint device that is not screen-compatible.

.. seealso:: :ref:`qfontinfo-checking-for-the-existence-of-a-font`.

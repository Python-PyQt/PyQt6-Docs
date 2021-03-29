.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: (const QFont&)
    :digest: 527bdfb576b0e04ea01916b312e23031

Constructs a font info object for *font*.

The font must be screen-compatible, i.e. a font you use when drawing text in `widgets <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtGui.QPixmap`, not :sip:ref:`~PyQt6.QtGui.QPicture` or :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`.

The font info object holds the information for the font that is passed in the constructor at the time it is created, and is not updated if the font's attributes are changed later.

Use :sip:ref:`~PyQt6.QtGui.QPainter.fontInfo` to get the font info when painting. This will give correct results also when painting on paint device that is not screen-compatible.

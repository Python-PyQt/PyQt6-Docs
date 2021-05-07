.. sip:method-description::
    :status: todo
    :pysig: e4f58c0e503ef85a9cd66ac982d689a2
    :realsig: (const QPainterPath&,const QBrush&)
    :digest: 2c6ca5615da8aba2111307b1bc1d75b7

Fills the given *path* using the given *brush*. The outline is not drawn.

Alternatively, you can specify a :sip:ref:`~PyQt6.QtGui.QColor` instead of a :sip:ref:`~PyQt6.QtGui.QBrush`; the :sip:ref:`~PyQt6.QtGui.QBrush` constructor (taking a :sip:ref:`~PyQt6.QtGui.QColor` argument) will automatically create a solid pattern brush.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPath`.

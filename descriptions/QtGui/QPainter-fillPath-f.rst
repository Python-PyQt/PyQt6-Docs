.. sip:method-description::
    :status: todo
    :pysig: 857130e5c97129825c1d6e82e4bec83d
    :realsig: (const QPainterPath&,const QBrush&)
    :digest: 2c6ca5615da8aba2111307b1bc1d75b7

Fills the given *path* using the given *brush*. The outline is not drawn.

Alternatively, you can specify a :sip:ref:`~PyQt6.QtGui.QColor` instead of a :sip:ref:`~PyQt6.QtGui.QBrush`; the :sip:ref:`~PyQt6.QtGui.QBrush` constructor (taking a :sip:ref:`~PyQt6.QtGui.QColor` argument) will automatically create a solid pattern brush.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPath`.

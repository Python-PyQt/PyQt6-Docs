.. sip:method-description::
    :status: todo
    :pysig: 64902a95c5084fe9e795ea67d3772d12
    :realsig: (const QRect&)
    :digest: a3863688dbf9ed0714c6118c55558bb3

Renders the widget into a pixmap restricted by the given *rectangle*. If the widget has any children, then they are also painted in the appropriate positions.

If a rectangle with an invalid size is specified (the default), the entire widget is painted.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.render`, :sip:ref:`~PyQt6.QtGui.QPixmap`.

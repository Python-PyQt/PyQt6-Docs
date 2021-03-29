.. sip:method-description::
    :status: todo
    :pysig: f0fdae4092719a6a97a2281c96095deb
    :realsig: (QPainter*,const QStyleOptionGraphicsItem*,QWidget*)
    :digest: d1ff06a7f87dd9fddc6acfd28fe9f4ec

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` to draw the window frame for windows using *painter*, *option*, and *widget*, in local coordinates. The base implementation uses the current style to render the frame and title bar.

You can reimplement this function in a subclass of `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ to provide custom rendering of the widget's window frame.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint`.

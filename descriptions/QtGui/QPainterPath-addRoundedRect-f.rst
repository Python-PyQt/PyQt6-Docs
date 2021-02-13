.. sip:method-description::
    :status: todo
    :pysig: e816b6776e7a221c79f10be7924128c5
    :realsig: (const QRectF&,qreal,qreal,Qt::SizeMode)
    :digest: 36b9557756d4d77f1320ca4fa9483683

Adds the given rectangle *rect* with rounded corners to the path.

The *xRadius* and *yRadius* arguments specify the radii of the ellipses defining the corners of the rounded rectangle. When *mode* is :sip:ref:`~PyQt6.QtCore.Qt.SizeMode.RelativeSize`, *xRadius* and *yRadius* are specified in percentage of half the rectangle's width and height respectively, and should be in the range 0.0 to 100.0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.addRect`.

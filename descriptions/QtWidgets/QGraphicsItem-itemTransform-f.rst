.. sip:method-description::
    :status: todo
    :pysig: 4c621ed8b224cb36a52f08c703393256
    :realsig: (const QGraphicsItem*,bool*) const
    :digest: 9cc96f08a53305d725f7f5438038579e

Returns a :sip:ref:`~PyQt6.QtGui.QTransform` that maps coordinates from this item to *other*. If *ok* is not null, and if there is no such transform, the boolean pointed to by *ok* will be set to false; otherwise it will be set to true.

This transform provides an alternative to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem` functions, by returning the appropriate transform so that you can map shapes and coordinates yourself. It also helps you write more efficient code when repeatedly mapping between the same two items.

**Note:** In rare circumstances, there is no transform that maps between two items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapToItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mapFromItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.deviceTransform`.

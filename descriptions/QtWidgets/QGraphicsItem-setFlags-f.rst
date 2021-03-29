.. sip:method-description::
    :status: todo
    :pysig: a7931e1ede683081858094d4aa0f85d4
    :realsig: (QGraphicsItem::GraphicsItemFlags)
    :digest: 3e82cfc6adb3c766903320f1e06317ab

Sets the item flags to *flags*. All flags in *flags* are enabled; all flags not in *flags* are disabled.

If the item had focus and *flags* does not enable :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable`, the item loses focus as a result of calling this function. Similarly, if the item was selected, and *flags* does not enabled :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsSelectable`, the item is automatically unselected.

By default, no flags are enabled. (`QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ enables the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemSendsGeometryChanges` flag by default in order to track position changes.)

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.flags`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFlag`.

.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: eeca062eeaeaa003f6cdbaa037b767bb

Returns whether a layout should delete this item in its destructor. If its true, then the layout will delete it. If its false, then it is assumed that another object has the ownership of it, and the layout won't delete this item.

If the item inherits both :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` (such as `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ does) the item is really part of two ownership hierarchies. This property informs what the layout should do with its child items when it is destructed. In the case of `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_, it is preferred that when the layout is deleted it won't delete its children (since they are also part of the graphics item hierarchy).

By default this value is initialized to false in :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`, but it is overridden by `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ to return true. This is because `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ is not normally part of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` hierarchy, so the parent layout should delete it. Subclasses might override this default behaviour by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setOwnedByLayout`\ (true).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setOwnedByLayout`.

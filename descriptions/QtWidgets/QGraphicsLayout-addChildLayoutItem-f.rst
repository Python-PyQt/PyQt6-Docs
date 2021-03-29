.. sip:method-description::
    :status: todo
    :pysig: 9e054189deef3e3f960ae3f2f2322951
    :realsig: (QGraphicsLayoutItem*)
    :digest: b649c496769c0d50b36c361a6337155c

This function is a convenience function provided for custom layouts, and will go through all items in the layout and reparent their graphics items to the closest `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ ancestor of the layout.

If *layoutItem* is already in a different layout, it will be removed from that layout.

If custom layouts want special behaviour they can ignore to use this function, and implement their own behaviour.

.. seealso:: graphicsItem().

.. sip:method-description::
    :status: todo
    :pysig: 2b90a6543f67fd907efed8827c7fc4c2
    :realsig: (const QRectF&,int,int)
    :digest: 56b1ef12ae0c764d8dc45469663a648d

If this item is part of a scene that is viewed by a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`, this convenience function will attempt to scroll the view to ensure that *rect* is visible inside the view's viewport. If *rect* is a null rect (the default), :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` will default to the item's bounding rect. *xmargin* and *ymargin* are the number of pixels the view should use for margins.

If the specified rect cannot be reached, the contents are scrolled to the nearest valid position.

If this item is not viewed by a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.ensureVisible`.

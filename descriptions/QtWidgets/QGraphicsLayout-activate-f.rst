.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cb56b98c4b3ec6f6e245e330e0799ab6

Activates the layout, causing all items in the layout to be immediately rearranged. This function is based on calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.count` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.itemAt`, and then calling setGeometry() on all items sequentially. When activated, the layout will adjust its geometry to its parent's contentsRect(). The parent will then invalidate any layout of its own.

If called in sequence or recursively, e.g., by one of the arranged items in response to being resized, this function will do nothing.

Note that the layout is free to use geometry caching to optimize this process. To forcefully invalidate any such cache, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate` before calling .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate`.

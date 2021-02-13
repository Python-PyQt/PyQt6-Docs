.. sip:method-description::
    :status: todo
    :pysig: d79802a45034fa3f86d39a4b9620765c
    :realsig: (const QPoint&) const
    :digest: 4c4f61177fccf0639c36636e965e25a8

Returns the item at position *pos*, which is in viewport coordinates. If there are several items at this position, this function returns the topmost item.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsview.py
    :lines: 126-133

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`, Sorting.

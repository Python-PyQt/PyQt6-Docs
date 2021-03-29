.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 722564b0d16ebe9ef0a46390df6a1edf

Prepares the item for a geometry change. Call this function before changing the bounding rect of an item to keep :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`'s index up to date.

will call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update` if this is necessary.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 241-247

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`.

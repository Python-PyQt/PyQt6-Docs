.. sip:method-description::
    :status: todo
    :pysig: 8126c0d3c23084e71f42662acc36a74c
    :realsig: (QGraphicsItem::GraphicsItemChange,const QVariant&)
    :digest: cb5942a92c6d7a9604ac0a4e543d7e38

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` to notify custom items that some part of the item's state changes. By reimplementing this function, you can react to a change, and in some cases (depending on *change*), adjustments can be made.

*change* is the parameter of the item that is changing. *value* is the new value; the type of the value depends on *change*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 222-236

The default implementation does nothing, and returns *value*.

Note: Certain :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` functions cannot be called in a reimplementation of this function; see the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.GraphicsItemChange` documentation for details.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.GraphicsItemChange`.

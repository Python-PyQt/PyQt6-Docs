.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: () const
    :digest: 9856eb35a2e6a879059731b23cf9c601

Returns the item's panel, or ``nullptr`` if this item does not have a panel. If the item is a panel, it will return itself. Otherwise it will return the closest ancestor that is a panel.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isPanel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsPanel`.

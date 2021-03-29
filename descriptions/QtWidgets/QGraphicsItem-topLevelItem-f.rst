.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: () const
    :digest: 1d1d2224c1723dafe218ccebc5854670

Returns this item's top-level item. The top-level item is the item's topmost ancestor item whose parent is ``nullptr``. If an item has no parent, its own pointer is returned (i.e., a top-level item is its own top-level item).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.parentItem`.

.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 56ae8768f43a6e063d04617c59957a74

Returns ``true`` if this item is empty, i.e whether it has no content and should not occupy any space.

The default implementation returns ``true`` true if the item has been hidden, unless its :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizePolicy` has retainSizeWhenHidden set to ``true``

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizePolicy`.

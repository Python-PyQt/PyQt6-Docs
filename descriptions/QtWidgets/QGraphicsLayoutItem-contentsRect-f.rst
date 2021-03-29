.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 5afe4f0b01c4f2bd376c687fecca4b4c

Returns the contents rect in local coordinates.

The contents rect defines the subrectangle used by an associated layout when arranging subitems. This function is a convenience function that adjusts the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.geometry` by its contents margins. Note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.getContentsMargins` is a virtual function that you can reimplement to return the item's contents margins.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.getContentsMargins`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.geometry`.

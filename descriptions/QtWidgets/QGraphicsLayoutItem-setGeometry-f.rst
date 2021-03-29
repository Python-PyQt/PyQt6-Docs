.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: 9f6c1c0dfda209269427008bd2207f40

This virtual function sets the geometry of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` to *rect*, which is in parent coordinates (e.g., the top-left corner of *rect* is equivalent to the item's position in parent coordinates).

You must reimplement this function in a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` to receive geometry updates. The layout will call this function when it does a rearrangement.

If *rect* is outside of the bounds of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.minimumSize` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.maximumSize`, it will be adjusted to its closest size so that it is within the legal bounds.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.geometry`.

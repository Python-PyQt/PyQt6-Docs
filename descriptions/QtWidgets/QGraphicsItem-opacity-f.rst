.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 209de0a419965b11dfb99f8e120e3483

Returns this item's local opacity, which is between 0.0 (transparent) and 1.0 (opaque). This value is combined with parent and ancestor values into the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.effectiveOpacity`. The effective opacity decides how the item is rendered and also affects its visibility when queried by functions such as :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items`.

The opacity property decides the state of the painter passed to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function. If the item is cached, i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache`, the effective property will be applied to the item's cache as it is rendered.

The default opacity is 1.0; fully opaque.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setOpacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIgnoresParentOpacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemDoesntPropagateOpacityToChildren`.

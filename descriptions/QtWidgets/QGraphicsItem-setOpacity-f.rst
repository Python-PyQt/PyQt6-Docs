.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 416682b2a115e2e5f6eb491efd9c4ab3

Sets this item's local *opacity*, between 0.0 (transparent) and 1.0 (opaque). The item's local opacity is combined with parent and ancestor opacities into the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.effectiveOpacity`.

By default, opacity propagates from parent to child, so if a parent's opacity is 0.5 and the child is also 0.5, the child's effective opacity will be 0.25.

The opacity property decides the state of the painter passed to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function. If the item is cached, i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache`, the effective property will be applied to the item's cache as it is rendered.

There are two item flags that affect how the item's opacity is combined with the parent: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIgnoresParentOpacity` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemDoesntPropagateOpacityToChildren`.

**Note:** Setting the opacity of an item to 0 will not make the item invisible (according to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible`), but the item will be treated like an invisible one. See the documentation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setVisible` for more information.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.opacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.effectiveOpacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setVisible`.

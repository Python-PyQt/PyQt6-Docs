.. sip:method-description::
    :status: todo
    :pysig: df613d498a3566ff2e6e5ccd24e1403e
    :realsig: (QGraphicsLayoutItem*,int)
    :digest: e784cbdd239c8af8394a37e0d2172bc2

Sets the stretch factor for *item* to *stretch*. If an item's stretch factor changes, this function will invalidate the layout.

Setting *stretch* to 0 removes the stretch factor from the item, and is effectively equivalent to setting *stretch* to 1.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.stretchFactor`.

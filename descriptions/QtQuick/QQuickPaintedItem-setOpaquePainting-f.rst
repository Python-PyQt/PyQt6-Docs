.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: fd096e31c4c669e493acc6673ed7fecf

If *opaque* is true, the item is opaque; otherwise, it is considered as translucent.

Opaque items are not blended with the rest of the scene, you should set this to true if the content of the item is opaque to speed up rendering.

By default, painted items are not opaque.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.opaquePainting`.

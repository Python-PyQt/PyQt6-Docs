.. sip:method-description::
    :status: todo
    :pysig: 06402b162572f668d054f99bc1104063
    :realsig: (const QGraphicsItem*) const
    :digest: dbc9768e3500684400c94939edd67562

Returns ``true`` if the item is visible to *parent*; otherwise, false is returned. *parent* can be ``nullptr``, in which case this function will return whether the item is visible to the scene or not.

An item may not be visible to its ancestors even if :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` is true. It may also be visible to its ancestors even if :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` is false. If any ancestor is hidden, the item itself will be implicitly hidden, in which case this function will return false.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setVisible`.

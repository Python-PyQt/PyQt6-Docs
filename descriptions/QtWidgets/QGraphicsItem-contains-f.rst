.. sip:method-description::
    :status: todo
    :pysig: 70fdb46d124e02d8a4f903d26e7c1cfc
    :realsig: (const QPointF&) const
    :digest: af5ee9d02a858b0e84895c63351b59ba

Returns ``true`` if this item contains *point*, which is in local coordinates; otherwise, false is returned. It is most often called from :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` to determine what item is under the cursor, and for that reason, the implementation of this function should be as light-weight as possible.

By default, this function calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`, but you can reimplement it in a subclass to provide a (perhaps more efficient) implementation.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithPath`.

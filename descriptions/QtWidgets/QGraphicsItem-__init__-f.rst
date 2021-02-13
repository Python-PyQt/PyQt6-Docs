.. sip:method-description::
    :status: todo
    :pysig: dee7591f11a028948c34d781226fc76c
    :realsig: (QGraphicsItem*)
    :digest: bb57f3c4deae86b633717ed5bc7a8825

Constructs a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` with the given *parent* item. It does not modify the parent object returned by :sip:ref:`~PyQt6.QtCore.QObject.parent`.

If *parent* is ``nullptr``, you can add the item to a scene by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`. The item will then become a top-level item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setParentItem`.

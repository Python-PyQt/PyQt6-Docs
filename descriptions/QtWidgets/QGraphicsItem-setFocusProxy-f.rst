.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: f114ae7777f794a0abe52d24e8822310

Sets the item's focus proxy to *item*.

If an item has a focus proxy, the focus proxy will receive input focus when the item gains input focus. The item itself will still have focus (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasFocus` will return true), but only the focus proxy will receive the keyboard input.

A focus proxy can itself have a focus proxy, and so on. In such case, keyboard input will be handled by the outermost focus proxy.

The focus proxy *item* must belong to the same scene as this item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusProxy`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasFocus`.

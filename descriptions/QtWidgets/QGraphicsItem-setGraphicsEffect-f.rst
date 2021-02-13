.. sip:method-description::
    :status: todo
    :pysig: 64a1e5fb21bbbebf6c8e03fbd369c42e
    :realsig: (QGraphicsEffect*)
    :digest: db935eea476ad308f14dcfb0e9ed8ad9

Sets *effect* as the item's effect. If there already is an effect installed on this item, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` will delete the existing effect before installing the new *effect*. You can delete an existing effect by calling (``nullptr``).

If *effect* is the installed effect on a different item,  will remove the effect from the item and install it on this item.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` takes ownership of *effect*.

**Note:** This function will apply the effect on itself and all its children.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.graphicsEffect`.

.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: 3114e0cc45b3e3186c018febcfdefaa9

This virtual function returns a shape representing the area where this item is opaque. An area is opaque if it is filled using an opaque brush or color (i.e., not transparent).

This function is used by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isObscuredBy`, which is called by underlying items to determine if they are obscured by this item.

The default implementation returns an empty :sip:ref:`~PyQt6.QtGui.QPainterPath`, indicating that this item is completely transparent and does not obscure any other items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isObscuredBy`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isObscured`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`.

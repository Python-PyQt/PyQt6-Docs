.. sip:method-description::
    :status: todo
    :pysig: 09e612eb66bcc1ae6053c82846817e48
    :realsig: () const
    :digest: 3e2e2bcca81d3b00939b0f24fdb44ce2

Returns the cursor shape for this item.

The mouse cursor will assume this shape when it is over this item, unless an override cursor is set. See the :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` for a range of useful shapes.

If no cursor shape has been set this returns a cursor with the :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.ArrowCursor` shape, however another cursor shape may be displayed if an overlapping item has a valid cursor.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.setCursor`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.unsetCursor`.

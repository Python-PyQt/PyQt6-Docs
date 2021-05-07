.. sip:method-description::
    :status: todo
    :pysig: 54325e9368999a85b6b186618ee81876
    :realsig: () const
    :digest: 8939e494f417d0bcc4c20182bcd294fe

Returns the mouse buttons accepted by this item.

The default value is :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.NoButton`; that is, no mouse buttons are accepted.

If an item does not accept the mouse button for a particular mouse event, the mouse event will not be delivered to the item and will be delivered to the next item in the item hierarchy instead.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.setAcceptedMouseButtons`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptTouchEvents`.

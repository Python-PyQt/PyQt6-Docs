.. sip:method-description::
    :status: todo
    :pysig: 0222541eefb25af4386c5601c68ff978
    :realsig: () const
    :digest: 8939e494f417d0bcc4c20182bcd294fe

Returns the mouse buttons accepted by this item.

The default value is :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton`; that is, no mouse buttons are accepted.

If an item does not accept the mouse button for a particular mouse event, the mouse event will not be delivered to the item and will be delivered to the next item in the item hierarchy instead.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.setAcceptedMouseButtons`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptTouchEvents`.

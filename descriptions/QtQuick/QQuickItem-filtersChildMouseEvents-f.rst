.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: b0863bf1bbf1d2f86add926cb6159a6e

Returns whether pointer events intended for this item's children should be filtered through this item.

If both this item and a child item have :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptTouchEvents` ``true``, then when a touch interaction occurs, this item will filter the touch event. But if either this item or the child cannot handle touch events, :sip:ref:`~PyQt6.QtQuick.QQuickItem.childMouseEventFilter` will be called with a synthesized mouse event.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.setFiltersChildMouseEvents`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.childMouseEventFilter`.

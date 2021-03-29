.. sip:method-description::
    :status: todo
    :pysig: d6ec79160519f7a35e42470ede097c04
    :realsig: (Qt::GestureType,bool)
    :digest: cb18b9d5e2e0c8298ecc02382acfaeaa

Sets the accept flag of the given *gestureType* object to the specified *value*.

Setting the accept flag indicates that the event receiver wants to receive gestures of the specified type, *gestureType*. Unwanted gestures may be propagated to the parent widget.

By default, gestures in events of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.Gesture` are accepted, and gestures in :sip:ref:`~PyQt6.QtCore.QEvent.Type.GestureOverride` events are ignored.

For convenience, the accept flag can also be set with :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.accept`, and cleared with :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.ignore`.

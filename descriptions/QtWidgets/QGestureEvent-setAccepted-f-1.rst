.. sip:method-description::
    :status: todo
    :pysig: daa73b54f89fcf687e20bc2879821f7d
    :realsig: (QGesture*,bool)
    :digest: 27d975f03a62ccd005ec2f15119362c3

Sets the accept flag of the given *gesture* object to the specified *value*.

Setting the accept flag indicates that the event receiver wants the *gesture*. Unwanted gestures may be propagated to the parent widget.

By default, gestures in events of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.Gesture` are accepted, and gestures in :sip:ref:`~PyQt6.QtCore.QEvent.Type.GestureOverride` events are ignored.

For convenience, the accept flag can also be set with :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.accept`, and cleared with :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.ignore`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.isAccepted`.

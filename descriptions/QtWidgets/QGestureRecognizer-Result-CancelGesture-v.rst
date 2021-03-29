.. sip:enum-member-description::
    :status: todo
    :value: 0x0010
    :realname: QGestureRecognizer::ResultFlag::CancelGesture
    :digest: 119aacec65f0bbfaf596416cc5232265

The event made it clear that it is not a gesture. If the gesture recognizer was in GestureTriggered state before, then the gesture is canceled and the appropriate :sip:ref:`~PyQt6.QtWidgets.QGesture` object will be delivered to the target as a part of a :sip:ref:`~PyQt6.QtWidgets.QGestureEvent`.

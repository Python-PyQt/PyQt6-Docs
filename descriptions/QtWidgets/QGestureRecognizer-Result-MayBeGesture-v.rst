.. sip:enum-member-description::
    :status: todo
    :value: 0x0002
    :realname: QGestureRecognizer::ResultFlag::MayBeGesture
    :digest: ed753fd5cf65256400317659b19af8d0

The event changed the internal state of the recognizer, but it isn't clear yet if it is a gesture or not. The recognizer needs to filter more events to decide. Gesture recognizers in the MayBeGesture state may be reset automatically if they take too long to recognize gestures.

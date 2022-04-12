.. sip:method-description::
    :status: todo
    :pysig: e063d6133994927b3fb8068d30b5ffaf
    :realsig: (QObject*,QScroller::ScrollerGestureType)
    :digest: babf3c3847e3cda3873ad3a246fd9554

Registers a custom scroll gesture recognizer, grabs it for the *target* and returns the resulting gesture type. If *scrollGestureType* is set to :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType.TouchGesture` the gesture triggers on touch events. If it is set to one of :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType.LeftMouseButtonGesture`, :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType.RightMouseButtonGesture` or :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType.MiddleMouseButtonGesture` it triggers on mouse events of the corresponding button.

Only one scroll gesture can be active on a single object at the same time. If you call this function twice on the same object, it will ungrab the existing gesture before grabbing the new one.

**Note:** To avoid unwanted side-effects, mouse events are consumed while the gesture is triggered. Since the initial mouse press event is not consumed, the gesture sends a fake mouse release event at the global position ``(INT_MIN, INT_MIN)``. This ensures that internal states of the widget that received the original mouse press are consistent.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.ungrabGesture`, :sip:ref:`~PyQt6.QtWidgets.QScroller.grabbedGesture`.

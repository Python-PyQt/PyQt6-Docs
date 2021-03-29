.. sip:method-description::
    :status: todo
    :pysig: 68829d2eb99d1d58831af2a1eab8e0c2
    :realsig: (QMouseEvent*)
    :digest: 880f53e60be7444f6d42dfd8545a799a

This event handler can be reimplemented in a subclass to receive mouse press events for an item. The event information is provided by the *event* parameter.

In order to receive mouse press events, :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptedMouseButtons` must return the relevant mouse button.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

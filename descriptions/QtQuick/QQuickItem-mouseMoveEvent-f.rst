.. sip:method-description::
    :status: todo
    :pysig: 68829d2eb99d1d58831af2a1eab8e0c2
    :realsig: (QMouseEvent*)
    :digest: ed364d58d2d1a9890b4640b320c3a002

This event handler can be reimplemented in a subclass to receive mouse move events for an item. The event information is provided by the *event* parameter.

In order to receive mouse movement events, the preceding mouse press event must be accepted (by overriding :sip:ref:`~PyQt6.QtQuick.QQuickItem.mousePressEvent`, for example) and :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptedMouseButtons` must return the relevant mouse button.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

.. sip:method-description::
    :status: todo
    :pysig: 24febdf7a73512c6bc71fb43131ac94b
    :realsig: (const QByteArray&, void*, qintptr*)
    :digest: fe9e90850536f05c2adc33be767ae7f9

This special event handler can be reimplemented in a subclass to receive native platform events identified by *eventType* which are passed in the *message* parameter.

In your reimplementation of this function, if you want to stop the event being handled by Qt, return true and set *result*. The *result* parameter has meaning only on Windows. If you return false, this native event is passed back to Qt, which translates the event into a Qt event and sends it to the widget.

**Note:** Events are only delivered to this event handler if the widget has a native window handle.

**Note:** This function superseedes the event filter functions x11Event(), winEvent() and macEvent() of Qt 4.

+----------+-----------------------+------------------------+-------------+
| Platform | Event Type Identifier | Message Type           | Result Type |
+==========+=======================+========================+=============+
| Windows  | "windows_generic_MSG" | MSG \*                 | LRESULT     |
+----------+-----------------------+------------------------+-------------+
| macOS    | "NSEvent"             | NSEvent \*             |             |
+----------+-----------------------+------------------------+-------------+
| XCB      | "xcb_generic_event_t" | xcb_generic_event_t \* |             |
+----------+-----------------------+------------------------+-------------+

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`.

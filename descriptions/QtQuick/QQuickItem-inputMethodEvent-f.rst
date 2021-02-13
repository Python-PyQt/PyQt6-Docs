.. sip:method-description::
    :status: todo
    :pysig: 1892efa11dcd6bbbb9a3c11f9e2fe516
    :realsig: (QInputMethodEvent*)
    :digest: 3da4adf71b73242304b683b1493d6eee

This event handler can be reimplemented in a subclass to receive input method events for an item. The event information is provided by the *event* parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

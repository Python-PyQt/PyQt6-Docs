.. sip:method-description::
    :status: todo
    :pysig: a28d7c815182564df2c1abd853ad768a
    :realsig: (QFocusEvent*)
    :digest: 33732e1376e14bd4bf98a0c50edecc60

This event handler can be reimplemented in a subclass to receive focus-out events for an item. The event information is provided by the ``event`` parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

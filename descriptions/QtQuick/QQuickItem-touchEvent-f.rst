.. sip:method-description::
    :status: todo
    :pysig: ae425840737e62c5fe2527479513f771
    :realsig: (QTouchEvent*)
    :digest: 62cc0fc26e4d35fa4375d49fbf2110f2

This event handler can be reimplemented in a subclass to receive touch events for an item. The event information is provided by the *event* parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

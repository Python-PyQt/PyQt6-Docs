.. sip:method-description::
    :status: todo
    :pysig: ce3d9b4daef6744486b5f293221f93ba
    :realsig: (QKeyEvent*)
    :digest: 44a253af7230577a21a1a9387633c2a8

This event handler can be reimplemented in a subclass to receive key press events for an item. The event information is provided by the *event* parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

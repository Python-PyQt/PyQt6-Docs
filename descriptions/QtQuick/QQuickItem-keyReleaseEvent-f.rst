.. sip:method-description::
    :status: todo
    :pysig: ce3d9b4daef6744486b5f293221f93ba
    :realsig: (QKeyEvent*)
    :digest: ec1a2e259816aa00663c4aaf112cf9ca

This event handler can be reimplemented in a subclass to receive key release events for an item. The event information is provided by the *event* parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

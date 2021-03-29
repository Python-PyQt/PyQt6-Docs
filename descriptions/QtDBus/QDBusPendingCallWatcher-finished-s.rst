.. sip:signal-description::
    :status: todo
    :pysig: a5bd32620dd5141d3fdebe1ad320ef79
    :realsig: (QDBusPendingCallWatcher*)
    :digest: eef9a25f3f37af7284f3e3557d32c6a0

This signal is emitted when the pending call has finished and its reply is available. The *self* parameter is a pointer to the object itself, passed for convenience so that the slot can access the properties and determine the contents of the reply.

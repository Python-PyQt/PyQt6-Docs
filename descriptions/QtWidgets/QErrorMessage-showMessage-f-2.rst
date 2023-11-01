.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 3a219d746404a8d508ae7d0d7f3ede39

Shows the given message, *message*, and returns immediately. If the user has requested for the message not to be shown again, this function does nothing.

Normally, the message is displayed immediately. However, if there are pending messages, it will be queued to be displayed later.

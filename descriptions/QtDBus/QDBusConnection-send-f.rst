.. sip:method-description::
    :status: todo
    :pysig: c66c4e44933b33a1b9b4e8a997109b73
    :realsig: (const QDBusMessage&) const
    :digest: 8f38806f3be38608123643ef0420df91

Sends the *message* over this connection, without waiting for a reply. This is suitable for errors, signals, and return values as well as calls whose return values are not necessary.

Returns ``true`` if the message was queued successfully, false otherwise.

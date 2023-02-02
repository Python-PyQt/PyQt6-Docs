.. sip:method-description::
    :status: todo
    :pysig: 33b0db7fbb72cd3be749c3d8e5e1a1e2
    :realsig: (const QByteArray&,void*,qintptr*)
    :digest: 135767834630ec7773b05ff00c2ec3e7

Override this to handle platform dependent events. Will be given *eventType*, *message* and *result*.

This might make your application non-portable.

Should return true only if the event was handled.

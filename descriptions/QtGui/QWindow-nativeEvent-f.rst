.. sip:method-description::
    :status: todo
    :pysig: e735352e572b5c896d6b3314190c75ee
    :realsig: (const QByteArray&,void*,qintptr*)
    :digest: 135767834630ec7773b05ff00c2ec3e7

Override this to handle platform dependent events. Will be given *eventType*, *message* and *result*.

This might make your application non-portable.

Should return true only if the event was handled.

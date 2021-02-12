.. sip:method-description::
    :status: todo
    :pysig: 99e9e0ca74e2fed0a89a2d02283f374e
    :realsig: (QThread*)
    :digest: c778146b6cd5a20b226863a74c76a0e8

Returns a pointer to the event dispatcher object for the specified *thread*. If *thread* is ``nullptr``, the current thread is used. If no event dispatcher exists for the specified thread, this function returns ``nullptr``.

**Note:** If Qt is built without thread support, the *thread* argument is ignored.

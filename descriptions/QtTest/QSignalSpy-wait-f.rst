.. sip:method-description::
    :status: todo
    :pysig: 3693397ff4e0cae2d0a0152cd1722150
    :realsig: (int)
    :digest: 38d49828be62db2124d74bee9d60647d

This is an overloaded function, equivalent passing *timeout* to the chrono overload:

::

    wait(std::chrono::milliseconds{timeout});

Returns ``true`` if the signal was emitted at least once in *timeout*, otherwise returns ``false``.

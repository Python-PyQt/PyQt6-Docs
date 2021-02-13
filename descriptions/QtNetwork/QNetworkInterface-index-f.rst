.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 99d0ec1af7be9ce599f7dbfcf3cad3a5

Returns the interface system index, if known. This is an integer assigned by the operating system to identify this interface and it generally doesn't change. It matches the scope ID field in IPv6 addresses.

If the index isn't known, this function returns 0.

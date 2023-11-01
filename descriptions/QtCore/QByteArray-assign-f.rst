.. sip:method-description::
    :status: todo
    :pysig: b2cc0c4f8d9f710ef7e89ba9aa900aca
    :realsig: (QByteArrayView)
    :digest: 10f95f4852d821a090d63afda290a01a

Replaces the contents of this byte array with a copy of *v* and returns a reference to this byte array.

The size of this byte array will be equal to the size of *v*.

This function only allocates memory if the size of *v* exceeds the capacity of this byte array or this byte array is shared.

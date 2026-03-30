.. sip:method-description::
    :status: todo
    :pysig: c40911c4f3d9223bc9913f4c9d6fd94d
    :realsig: (QByteArrayView)
    :digest: 10f95f4852d821a090d63afda290a01a

Replaces the contents of this byte array with a copy of *v* and returns a reference to this byte array.

The size of this byte array will be equal to the size of *v*.

This function only allocates memory if the size of *v* exceeds the capacity of this byte array or this byte array is shared.

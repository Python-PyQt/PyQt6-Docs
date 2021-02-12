.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 27460f647858e173111fc1c3c8bc9e1b

Returns the maximum number of bytes that can be stored in the byte array without forcing a reallocation.

The sole purpose of this function is to provide a means of fine tuning :sip:ref:`~PyQt6.QtCore.QByteArray`'s memory usage. In general, you will rarely ever need to call this function. If you want to know how many bytes are in the byte array, call :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

**Note:** a statically allocated byte array will report a capacity of 0, even if it's not empty.

**Note:** The free space position in the allocated memory block is undefined. In other words, one should not assume that the free memory is always located after the initialized elements.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.reserve`, :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.

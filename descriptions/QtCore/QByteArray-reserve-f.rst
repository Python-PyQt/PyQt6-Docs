.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: 49d06e637668a290cf0662f0bba384d4

Attempts to allocate memory for at least *size* bytes.

If you know in advance how large the byte array will be, you can call this function, and if you call :sip:ref:`~PyQt6.QtCore.QByteArray.resize` often you are likely to get better performance.

If in doubt about how much space shall be needed, it is usually better to use an upper bound as *size*, or a high estimate of the most likely size, if a strict upper bound would be much bigger than this. If *size* is an underestimate, the array will grow as needed once the reserved size is exceeded, which may lead to a larger allocation than your best overestimate would have and will slow the operation that triggers it.

**Warning:**  reserves memory but does not change the size of the byte array. Accessing data beyond the end of the byte array is undefined behavior. If you need to access memory beyond the current end of the array, use :sip:ref:`~PyQt6.QtCore.QByteArray.resize`.

The sole purpose of this function is to provide a means of fine tuning :sip:ref:`~PyQt6.QtCore.QByteArray`'s memory usage. In general, you will rarely ever need to call this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`, :sip:ref:`~PyQt6.QtCore.QByteArray.capacity`.

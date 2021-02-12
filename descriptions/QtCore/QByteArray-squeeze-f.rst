.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 42c312eac9a2b5797bdf96bb1c3c431b

Releases any memory not required to store the array's data.

The sole purpose of this function is to provide a means of fine tuning :sip:ref:`~PyQt6.QtCore.QByteArray`'s memory usage. In general, you will rarely ever need to call this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.reserve`, :sip:ref:`~PyQt6.QtCore.QByteArray.capacity`.

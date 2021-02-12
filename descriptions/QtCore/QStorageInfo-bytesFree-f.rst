.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6746b99a3761fad52a1291461af04376

Returns the number of free bytes in a volume. Note that if there are quotas on the filesystem, this value can be larger than the value returned by :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesAvailable`.

Returns -1 if :sip:ref:`~PyQt6.QtCore.QStorageInfo` object is not valid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesTotal`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesAvailable`.

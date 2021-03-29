.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 4cdcce13b06232e36a5473f0af3314c0

Returns the size (in bytes) available for the current user. It returns the total size available if the user is the root user or a system administrator.

This size can be less than or equal to the free size returned by :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesFree` function.

Returns -1 if :sip:ref:`~PyQt6.QtCore.QStorageInfo` object is not valid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesTotal`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesFree`.

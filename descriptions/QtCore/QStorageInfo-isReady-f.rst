.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 48dfb4124ebfd02ca7fac1e479039733

Returns true if the current filesystem is ready to work; false otherwise. For example, false is returned if the CD volume is not inserted.

Note that :sip:ref:`~PyQt6.QtCore.QStorageInfo.fileSystemType`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.name`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesTotal`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesFree`, and :sip:ref:`~PyQt6.QtCore.QStorageInfo.bytesAvailable` will return invalid data until the volume is ready.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.isValid`.

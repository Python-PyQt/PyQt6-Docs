.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (qint64)
    :digest: 3cd679d29eac9858825257624fbb5ff4

Sets the file size (in bytes) *sz*. Returns ``true`` if the resize succeeds; false otherwise. If *sz* is larger than the file currently is, the new bytes will be set to 0; if *sz* is smaller, the file is simply truncated.

**Warning:** This function can fail if the file doesn't exist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileDevice.size`.

.. sip:enum-description::
    :status: todo
    :digest: 32998e6193032bd3cc28dba5577e7c74

The precision of floating point numbers used for reading/writing the data. This will only have an effect if the version of the data stream is :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Qt_4_6` or higher.

**Warning:** The floating point precision must be set to the same value on the object that writes and the object that reads the data stream.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.setFloatingPointPrecision`, :sip:ref:`~PyQt6.QtCore.QDataStream.floatingPointPrecision`.

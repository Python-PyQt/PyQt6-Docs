.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9cb3a2ac3fef9d0dbc53172269991f1a

Starts a new read transaction on the stream.

Defines a restorable point within the sequence of read operations. For sequential devices, read data will be duplicated internally to allow recovery in case of incomplete reads. For random-access devices, this function saves the current position of the stream. Call :sip:ref:`~PyQt6.QtCore.QDataStream.commitTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.rollbackTransaction`, or :sip:ref:`~PyQt6.QtCore.QDataStream.abortTransaction` to finish the current transaction.

Once a transaction is started, subsequent calls to this function will make the transaction recursive. Inner transactions act as agents of the outermost transaction (i.e., report the status of read operations to the outermost transaction, which can restore the position of the stream).

**Note:** Restoring to the point of the nested  call is not supported.

When an error occurs during a transaction (including an inner transaction failing), reading from the data stream is suspended (all subsequent read operations return empty/zero values) and subsequent inner transactions are forced to fail. Starting a new outermost transaction recovers from this state. This behavior makes it unnecessary to error-check every read operation separately.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.commitTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.rollbackTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.abortTransaction`.

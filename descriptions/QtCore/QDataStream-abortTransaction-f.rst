.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fcc6e742193811a358cd1d14bb955944

Aborts a read transaction.

This function is commonly used to discard the transaction after higher-level protocol errors or loss of stream synchronization.

If called on an inner transaction, aborting is delegated to the outermost transaction, and subsequently started inner transactions are forced to fail.

For the outermost transaction, discards the restoration point and any internally duplicated data of the stream. Will not affect the current read position of the stream.

Sets the status of the data stream to

+-----------------+-------------+
| Constant        | Description |
+=================+=============+
| ReadCorruptData | .           |
+-----------------+-------------+

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.startTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.commitTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.rollbackTransaction`.

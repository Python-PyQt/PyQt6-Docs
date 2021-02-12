.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e03c21e3277b5ecb39b350a7584da05a

Reverts a read transaction.

This function is commonly used to rollback the transaction when an incomplete read was detected prior to committing the transaction.

If called on an inner transaction, reverting is delegated to the outermost transaction, and subsequently started inner transactions are forced to fail.

For the outermost transaction, restores the stream data to the point of the :sip:ref:`~PyQt6.QtCore.QDataStream.startTransaction` call. If the data stream has read corrupt data or any of the inner transactions was aborted, this function aborts the transaction.

If the preceding stream operations were successful, sets the status of the data stream to

+-------------+-------------+
| Constant    | Description |
+=============+=============+
| ReadPastEnd | .           |
+-------------+-------------+

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.startTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.commitTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.abortTransaction`.

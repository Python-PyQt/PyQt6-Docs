.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: d7e52b175646f3571f8eb80128a3d389

Completes a read transaction. Returns ``true`` if no read errors have occurred during the transaction; otherwise returns ``false``.

If called on an inner transaction, committing will be postponed until the outermost commitTransaction(), :sip:ref:`~PyQt6.QtCore.QDataStream.rollbackTransaction`, or :sip:ref:`~PyQt6.QtCore.QDataStream.abortTransaction` call occurs.

Otherwise, if the stream status indicates reading past the end of the data, this function restores the stream data to the point of the :sip:ref:`~PyQt6.QtCore.QDataStream.startTransaction` call. When this situation occurs, you need to wait for more data to arrive, after which you start a new transaction. If the data stream has read corrupt data or any of the inner transactions was aborted, this function aborts the transaction.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.startTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.rollbackTransaction`, :sip:ref:`~PyQt6.QtCore.QDataStream.abortTransaction`.

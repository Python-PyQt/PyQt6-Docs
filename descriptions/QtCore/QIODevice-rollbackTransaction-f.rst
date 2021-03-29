.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 50b98e56157e450d92d40d88e7ff777d

Rolls back a read transaction.

Restores the input stream to the point of the :sip:ref:`~PyQt6.QtCore.QIODevice.startTransaction` call. This function is commonly used to rollback the transaction when an incomplete read was detected prior to committing the transaction.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.startTransaction`, :sip:ref:`~PyQt6.QtCore.QIODevice.commitTransaction`.

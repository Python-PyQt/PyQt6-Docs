.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 80b19298ee993ddfa2b7b530dbff910c

Starts a new read transaction on the device.

Defines a restorable point within the sequence of read operations. For sequential devices, read data will be duplicated internally to allow recovery in case of incomplete reads. For random-access devices, this function saves the current position. Call :sip:ref:`~PyQt6.QtCore.QIODevice.commitTransaction` or :sip:ref:`~PyQt6.QtCore.QIODevice.rollbackTransaction` to finish the transaction.

**Note:** Nesting transactions is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.commitTransaction`, :sip:ref:`~PyQt6.QtCore.QIODevice.rollbackTransaction`.

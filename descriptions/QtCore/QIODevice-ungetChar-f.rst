.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (char)
    :digest: 38bbf36c7ac6d561eb7df137a1244e95

Puts the character *c* back into the device, and decrements the current position unless the position is 0. This function is usually called to "undo" a :sip:ref:`~PyQt6.QtCore.QIODevice.getChar` operation, such as when writing a backtracking parser.

If *c* was not previously read from the device, the behavior is undefined.

**Note:** This function is not available while a transaction is in progress.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1cb49111a4a150a8c1afaec4b7e185e8

Releases the lock, by deleting the lock file.

Calling unlock() without locking the file first, does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.lock`, :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock`.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d653bca429434d916ffb85198f85f47e

Releases the lock, by deleting the lock file.

Calling  without locking the file first, does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.lock`, :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock`.

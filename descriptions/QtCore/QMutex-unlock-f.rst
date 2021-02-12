.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e33570fd2c7ab1a3c2697f399d644f5e

Unlocks the mutex. Attempting to unlock a mutex in a different thread to the one that locked it results in an error. Unlocking a mutex that is not locked results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`.

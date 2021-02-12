.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ad5b115ddcd554d9823fe4530e4c9579

Sets *staleLockTime* to be the time in milliseconds after which a lock file is considered stale. The default value is 30000, i.e. 30 seconds. If your application typically keeps the file locked for more than 30 seconds (for instance while saving megabytes of data for 2 minutes), you should set a bigger value using .

The value of *staleLockTime* is used by :sip:ref:`~PyQt6.QtCore.QLockFile.lock` and :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` in order to determine when an existing lock file is considered stale, i.e. left over by a crashed process. This is useful for the case where the PID got reused meanwhile, so one way to detect a stale lock file is by the fact that it has been around for a long time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.staleLockTime`.

.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: c9f9c8cdcdd34277b219c4f834e45735

Sets *staleLockTime* to be the time in milliseconds after which a lock file is considered stale. The default value is 30000, i.e. 30 seconds. If your application typically keeps the file locked for more than 30 seconds (for instance while saving megabytes of data for 2 minutes), you should set a bigger value using setStaleLockTime().

The value of *staleLockTime* is used by :sip:ref:`~PyQt6.QtCore.QLockFile.lock` and :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` in order to determine when an existing lock file is considered stale, i.e. left over by a crashed process. This is useful for the case where the PID got reused meanwhile, so one way to detect a stale lock file is by the fact that it has been around for a long time.

This is an overloaded function, equivalent to calling:

::

    setStaleLockTime(std::chrono::milliseconds{staleLockTime});

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.staleLockTime`.

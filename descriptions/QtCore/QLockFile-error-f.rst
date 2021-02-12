.. sip:method-description::
    :status: todo
    :pysig: c16598af5e879b350db2eeec4a08b61c
    :realsig: () const
    :digest: 0f3be09072dd1780ab53e5665bc930d7

Returns the lock file error status.

If :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` returns ``false``, this function can be called to find out the reason why the locking failed.

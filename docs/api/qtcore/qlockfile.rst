:orphan:

.. sip:class:: PyQt6.QtCore.QLockFile
    :description: QtCore/QLockFile-c.rst

    .. sip:enum:: PyQt6.QtCore.QLockFile.LockError
        :description: QtCore/QLockFile-LockError-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QLockFile.LockError.LockFailedError
            :description: QtCore/QLockFile-LockError-LockFailedError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLockFile.LockError.NoError
            :description: QtCore/QLockFile-LockError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLockFile.LockError.PermissionError
            :description: QtCore/QLockFile-LockError-PermissionError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QLockFile.LockError.UnknownError
            :description: QtCore/QLockFile-LockError-UnknownError-v.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.__init__
        :args:
            Optional[str]
        :description: QtCore/QLockFile-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLockFile.LockError`
        :description: QtCore/QLockFile-error-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.fileName
        :returns:
            str
        :description: QtCore/QLockFile-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.getLockInfo
        :returns:
            bool
            int
            str
            str
        :description: QtCore/QLockFile-getLockInfo-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.isLocked
        :returns:
            bool
        :description: QtCore/QLockFile-isLocked-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.lock
        :returns:
            bool
        :description: QtCore/QLockFile-lock-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.removeStaleLockFile
        :returns:
            bool
        :description: QtCore/QLockFile-removeStaleLockFile-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.setStaleLockTime
        :args:
            int
        :description: QtCore/QLockFile-setStaleLockTime-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.staleLockTime
        :returns:
            int
        :description: QtCore/QLockFile-staleLockTime-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.tryLock
        :args:
            timeout: int = 0
        :returns:
            bool
        :description: QtCore/QLockFile-tryLock-f.rst

    .. sip:method:: PyQt6.QtCore.QLockFile.unlock
        :description: QtCore/QLockFile-unlock-f.rst

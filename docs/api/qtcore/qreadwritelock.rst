:orphan:

.. sip:class:: PyQt6.QtCore.QReadWriteLock
    :description: QtCore/QReadWriteLock-c.rst

    .. sip:enum:: PyQt6.QtCore.QReadWriteLock.RecursionMode
        :description: QtCore/QReadWriteLock-RecursionMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QReadWriteLock.RecursionMode.NonRecursive
            :description: QtCore/QReadWriteLock-RecursionMode-NonRecursive-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QReadWriteLock.RecursionMode.Recursive
            :description: QtCore/QReadWriteLock-RecursionMode-Recursive-v.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.__init__
        :args:
            recursionMode: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.RecursionMode` = :sip:ref:`~PyQt6.QtCore.QReadWriteLock.RecursionMode.NonRecursive`
        :description: QtCore/QReadWriteLock-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.lockForRead
        :description: QtCore/QReadWriteLock-lockForRead-f.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.lockForWrite
        :description: QtCore/QReadWriteLock-lockForWrite-f.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.tryLockForRead
        :args:
            timeout: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` = {}
        :returns:
            bool
        :description: QtCore/QReadWriteLock-tryLockForRead-f-2.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.tryLockForRead
        :args:
            int
        :returns:
            bool
        :description: QtCore/QReadWriteLock-tryLockForRead-f-1.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.tryLockForWrite
        :args:
            timeout: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` = {}
        :returns:
            bool
        :description: QtCore/QReadWriteLock-tryLockForWrite-f-2.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.tryLockForWrite
        :args:
            int
        :returns:
            bool
        :description: QtCore/QReadWriteLock-tryLockForWrite-f-1.rst

    .. sip:method:: PyQt6.QtCore.QReadWriteLock.unlock
        :description: QtCore/QReadWriteLock-unlock-f.rst

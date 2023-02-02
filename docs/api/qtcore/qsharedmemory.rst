:orphan:

.. sip:class:: PyQt6.QtCore.QSharedMemory
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QSharedMemory-c.rst

    .. sip:enum:: PyQt6.QtCore.QSharedMemory.AccessMode
        :description: QtCore/QSharedMemory-AccessMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.AccessMode.ReadOnly
            :description: QtCore/QSharedMemory-AccessMode-ReadOnly-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.AccessMode.ReadWrite
            :description: QtCore/QSharedMemory-AccessMode-ReadWrite-v.rst

    .. sip:enum:: PyQt6.QtCore.QSharedMemory.SharedMemoryError
        :description: QtCore/QSharedMemory-SharedMemoryError-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.AlreadyExists
            :description: QtCore/QSharedMemory-SharedMemoryError-AlreadyExists-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.InvalidSize
            :description: QtCore/QSharedMemory-SharedMemoryError-InvalidSize-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.KeyError
            :description: QtCore/QSharedMemory-SharedMemoryError-KeyError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.LockError
            :description: QtCore/QSharedMemory-SharedMemoryError-LockError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.NoError
            :description: QtCore/QSharedMemory-SharedMemoryError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.NotFound
            :description: QtCore/QSharedMemory-SharedMemoryError-NotFound-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.OutOfResources
            :description: QtCore/QSharedMemory-SharedMemoryError-OutOfResources-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.PermissionDenied
            :description: QtCore/QSharedMemory-SharedMemoryError-PermissionDenied-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSharedMemory.SharedMemoryError.UnknownError
            :description: QtCore/QSharedMemory-SharedMemoryError-UnknownError-v.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSharedMemory-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSharedMemory-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.attach
        :args:
            mode: :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode.ReadWrite`
        :returns:
            bool
        :description: QtCore/QSharedMemory-attach-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.constData
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QSharedMemory-constData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.create
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode.ReadWrite`
        :returns:
            bool
        :description: QtCore/QSharedMemory-create-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.data
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QSharedMemory-data-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.detach
        :returns:
            bool
        :description: QtCore/QSharedMemory-detach-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSharedMemory.SharedMemoryError`
        :description: QtCore/QSharedMemory-error-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.errorString
        :returns:
            str
        :description: QtCore/QSharedMemory-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.isAttached
        :returns:
            bool
        :description: QtCore/QSharedMemory-isAttached-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.key
        :returns:
            str
        :description: QtCore/QSharedMemory-key-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.lock
        :returns:
            bool
        :description: QtCore/QSharedMemory-lock-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.nativeKey
        :returns:
            str
        :description: QtCore/QSharedMemory-nativeKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.setKey
        :args:
            str
        :description: QtCore/QSharedMemory-setKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.setNativeKey
        :args:
            str
        :description: QtCore/QSharedMemory-setNativeKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.size
        :returns:
            int
        :description: QtCore/QSharedMemory-size-f.rst

    .. sip:method:: PyQt6.QtCore.QSharedMemory.unlock
        :returns:
            bool
        :description: QtCore/QSharedMemory-unlock-f.rst

:orphan:

.. sip:class:: PyQt6.QtCore.QSystemSemaphore
    :description: QtCore/QSystemSemaphore-c.rst

    .. sip:enum:: PyQt6.QtCore.QSystemSemaphore.AccessMode
        :description: QtCore/QSystemSemaphore-AccessMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.AccessMode.Create
            :description: QtCore/QSystemSemaphore-AccessMode-Create-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.AccessMode.Open
            :description: QtCore/QSystemSemaphore-AccessMode-Open-v.rst

    .. sip:enum:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError
        :description: QtCore/QSystemSemaphore-SystemSemaphoreError-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.AlreadyExists
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-AlreadyExists-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.KeyError
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-KeyError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.NoError
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.NotFound
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-NotFound-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.OutOfResources
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-OutOfResources-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.PermissionDenied
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-PermissionDenied-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError.UnknownError
            :description: QtCore/QSystemSemaphore-SystemSemaphoreError-UnknownError-v.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`
            initialValue: int = 0
            mode: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`
        :description: QtCore/QSystemSemaphore-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.__init__
        :args:
            Optional[str]
            initialValue: int = 0
            mode: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`
        :description: QtCore/QSystemSemaphore-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.acquire
        :returns:
            bool
        :description: QtCore/QSystemSemaphore-acquire-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError`
        :description: QtCore/QSystemSemaphore-error-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.errorString
        :returns:
            str
        :description: QtCore/QSystemSemaphore-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.isKeyTypeSupported
        :args:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type`
        :returns:
            bool
        :static:
        :description: QtCore/QSystemSemaphore-isKeyTypeSupported-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.key
        :returns:
            str
        :description: QtCore/QSystemSemaphore-key-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.legacyNativeKey
        :args:
            Optional[str]
            type: :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type` = QNativeIpcKey.legacyDefaultTypeForOs()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`
        :static:
        :description: QtCore/QSystemSemaphore-legacyNativeKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.nativeIpcKey
        :returns:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`
        :description: QtCore/QSystemSemaphore-nativeIpcKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.platformSafeKey
        :args:
            Optional[str]
            type: :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type` = QNativeIpcKey.DefaultTypeForOs
        :returns:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`
        :static:
        :description: QtCore/QSystemSemaphore-platformSafeKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.release
        :args:
            n: int = 1
        :returns:
            bool
        :description: QtCore/QSystemSemaphore-release-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.setKey
        :args:
            Optional[str]
            initialValue: int = 0
            mode: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`
        :description: QtCore/QSystemSemaphore-setKey-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.setNativeKey
        :args:
            :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`
            initialValue: int = 0
            mode: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`
        :description: QtCore/QSystemSemaphore-setNativeKey-f.rst

    .. sip:method:: PyQt6.QtCore.QSystemSemaphore.setNativeKey
        :args:
            Optional[str]
            initialValue: int = 0
            mode: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` = :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`
            type: :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type` = QNativeIpcKey.legacyDefaultTypeForOs()
        :description: QtCore/QSystemSemaphore-setNativeKey-f-1.rst

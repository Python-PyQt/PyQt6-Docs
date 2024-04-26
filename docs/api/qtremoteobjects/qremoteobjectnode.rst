:orphan:

.. sip:class:: PyQt6.QtRemoteObjects.QRemoteObjectNode
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtRemoteObjects/QRemoteObjectNode-c.rst

    .. sip:enum:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode
        :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-e.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.HostUrlInvalid
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-HostUrlInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ListenFailed
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-ListenFailed-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.MissingObjectName
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-MissingObjectName-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.NodeIsNoServer
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-NodeIsNoServer-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.NoError
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.OperationNotValidOnClientNode
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-OperationNotValidOnClientNode-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ProtocolMismatch
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-ProtocolMismatch-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.RegistryAlreadyHosted
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-RegistryAlreadyHosted-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.RegistryNotAcquired
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-RegistryNotAcquired-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ServerAlreadyCreated
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-ServerAlreadyCreated-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.SocketAccessError
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-SocketAccessError-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.SourceNotRegistered
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-SourceNotRegistered-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode.UnintendedRegistryHosting
            :description: QtRemoteObjects/QRemoteObjectNode-ErrorCode-UnintendedRegistryHosting-v.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtRemoteObjects/QRemoteObjectNode-__init__-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtRemoteObjects/QRemoteObjectNode-__init__-f-1.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.acquireDynamic
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectDynamicReplica`
        :description: QtRemoteObjects/QRemoteObjectNode-acquireDynamic-f-1.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.acquireModel
        :args:
            Optional[str]
            action: :sip:ref:`~PyQt6.QtRemoteObjects.QtRemoteObjects.InitialAction` = :sip:ref:`~PyQt6.QtRemoteObjects.QtRemoteObjects.InitialAction.FetchRootSize`
            rolesHint: Iterable[int] = []
        :returns:
            :sip:ref:`~PyQt6.QtRemoteObjects.QAbstractItemModelReplica`
        :description: QtRemoteObjects/QRemoteObjectNode-acquireModel-f-1.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.addClientSideConnection
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtRemoteObjects/QRemoteObjectNode-addClientSideConnection-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.connectToNode
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectNode-connectToNode-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.heartbeatInterval
        :returns:
            int
        :description: QtRemoteObjects/QRemoteObjectNode-heartbeatInterval-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.instances
        :args:
            str
        :returns:
            List[str]
        :description: QtRemoteObjects/QRemoteObjectNode-instances-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.lastError
        :returns:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode`
        :description: QtRemoteObjects/QRemoteObjectNode-lastError-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.persistedStore
        :returns:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore`
        :description: QtRemoteObjects/QRemoteObjectNode-persistedStore-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.registry
        :returns:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry`
        :description: QtRemoteObjects/QRemoteObjectNode-registry-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.registryUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtRemoteObjects/QRemoteObjectNode-registryUrl-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.setHeartbeatInterval
        :args:
            int
        :description: QtRemoteObjects/QRemoteObjectNode-setHeartbeatInterval-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.setName
        :args:
            Optional[str]
        :description: QtRemoteObjects/QRemoteObjectNode-setName-f-1.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.setPersistedStore
        :args:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore`
        :description: QtRemoteObjects/QRemoteObjectNode-setPersistedStore-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.setRegistryUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectNode-setRegistryUrl-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtRemoteObjects/QRemoteObjectNode-timerEvent-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectNode.waitForRegistry
        :args:
            timeout: int = 30000
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectNode-waitForRegistry-f.rst

    .. sip:signal:: PyQt6.QtRemoteObjects.QRemoteObjectNode.error
        :args:
            :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.ErrorCode`
        :description: QtRemoteObjects/QRemoteObjectNode-error-s.rst

    .. sip:signal:: PyQt6.QtRemoteObjects.QRemoteObjectNode.heartbeatIntervalChanged
        :args:
            int
        :description: QtRemoteObjects/QRemoteObjectNode-heartbeatIntervalChanged-s.rst

    .. sip:signal:: PyQt6.QtRemoteObjects.QRemoteObjectNode.remoteObjectAdded
        :args:
            Tuple[Optional[str], :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectSourceLocationInfo`]
        :description: QtRemoteObjects/QRemoteObjectNode-remoteObjectAdded-s-1.rst

    .. sip:signal:: PyQt6.QtRemoteObjects.QRemoteObjectNode.remoteObjectRemoved
        :args:
            Tuple[Optional[str], :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectSourceLocationInfo`]
        :description: QtRemoteObjects/QRemoteObjectNode-remoteObjectRemoved-s-1.rst

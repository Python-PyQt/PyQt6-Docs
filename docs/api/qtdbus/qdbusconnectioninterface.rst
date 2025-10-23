:orphan:

.. sip:class:: PyQt6.QtDBus.QDBusConnectionInterface
    :inherits: :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface`
    :description: QtDBus/QDBusConnectionInterface-c.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnectionInterface.RegisterServiceReply
        :description: QtDBus/QDBusConnectionInterface-RegisterServiceReply-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.RegisterServiceReply.ServiceNotRegistered
            :description: QtDBus/QDBusConnectionInterface-RegisterServiceReply-ServiceNotRegistered-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.RegisterServiceReply.ServiceQueued
            :description: QtDBus/QDBusConnectionInterface-RegisterServiceReply-ServiceQueued-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.RegisterServiceReply.ServiceRegistered
            :description: QtDBus/QDBusConnectionInterface-RegisterServiceReply-ServiceRegistered-v.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions
        :description: QtDBus/QDBusConnectionInterface-ServiceQueueOptions-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions.DontQueueService
            :description: QtDBus/QDBusConnectionInterface-ServiceQueueOptions-DontQueueService-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions.QueueService
            :description: QtDBus/QDBusConnectionInterface-ServiceQueueOptions-QueueService-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions.ReplaceExistingService
            :description: QtDBus/QDBusConnectionInterface-ServiceQueueOptions-ReplaceExistingService-v.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions
        :description: QtDBus/QDBusConnectionInterface-ServiceReplacementOptions-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions.AllowReplacement
            :description: QtDBus/QDBusConnectionInterface-ServiceReplacementOptions-AllowReplacement-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions.DontAllowReplacement
            :description: QtDBus/QDBusConnectionInterface-ServiceReplacementOptions-DontAllowReplacement-v.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.activatableServiceNames
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-activatableServiceNames-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.connectNotify
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaMethod`
        :description: QtDBus/QDBusConnectionInterface-connectNotify-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.disconnectNotify
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaMethod`
        :description: QtDBus/QDBusConnectionInterface-disconnectNotify-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.isServiceRegistered
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-isServiceRegistered-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.registeredServiceNames
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-registeredServiceNames-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.registerService
        :args:
            Optional[str]
            qoption: :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions` = :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.ServiceQueueOptions.DontQueueService`
            roption: :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions` = :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions.DontAllowReplacement`
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-registerService-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.serviceCredentials
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-serviceCredentials-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.serviceOwner
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-serviceOwner-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.servicePid
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-servicePid-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.serviceUid
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-serviceUid-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.startService
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-startService-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnectionInterface.unregisterService
        :args:
            Optional[str]
        :returns:
            QDBusReply
        :description: QtDBus/QDBusConnectionInterface-unregisterService-f-1.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusConnectionInterface.callWithCallbackFailed
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusError`
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusConnectionInterface-callWithCallbackFailed-s.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusConnectionInterface.serviceOwnerChanged
        :args:
            Optional[str]
            Optional[str]
            Optional[str]
        :description: QtDBus/QDBusConnectionInterface-serviceOwnerChanged-s-1.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusConnectionInterface.serviceRegistered
        :args:
            Optional[str]
        :description: QtDBus/QDBusConnectionInterface-serviceRegistered-s-1.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusConnectionInterface.serviceUnregistered
        :args:
            Optional[str]
        :description: QtDBus/QDBusConnectionInterface-serviceUnregistered-s-1.rst

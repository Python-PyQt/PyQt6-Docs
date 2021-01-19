:orphan:

.. sip:class:: PyQt6.QtDBus.QDBusConnection
    :description: QtDBus/QDBusConnection-c.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnection.BusType
        :description: QtDBus/QDBusConnection-BusType-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.BusType.ActivationBus
            :description: QtDBus/QDBusConnection-BusType-ActivationBus-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.BusType.SessionBus
            :description: QtDBus/QDBusConnection-BusType-SessionBus-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.BusType.SystemBus
            :description: QtDBus/QDBusConnection-BusType-SystemBus-v.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnection.ConnectionCapabilities
        :description: QtDBus/QDBusConnection-ConnectionCapabilities-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.ConnectionCapabilities.UnixFileDescriptorPassing
            :description: QtDBus/QDBusConnection-ConnectionCapabilities-UnixFileDescriptorPassing-v.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnection.RegisterOptions
        :description: QtDBus/QDBusConnection-RegisterOptions-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAdaptors
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAdaptors-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllContents
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllContents-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllInvokables
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllInvokables-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllProperties
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllProperties-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllSignal
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllSignal-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllSignals
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllSignals-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAllSlots
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportAllSlots-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportChildObjects
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportChildObjects-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportNonScriptableContents
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportNonScriptableContents-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportNonScriptableInvokables
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportNonScriptableInvokables-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportNonScriptableProperties
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportNonScriptableProperties-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportNonScriptableSignals
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportNonScriptableSignals-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportNonScriptableSlots
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportNonScriptableSlots-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportScriptableContents
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportScriptableContents-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportScriptableInvokables
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportScriptableInvokables-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportScriptableProperties
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportScriptableProperties-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportScriptableSignals
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportScriptableSignals-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportScriptableSlots
            :description: QtDBus/QDBusConnection-RegisterOptions-ExportScriptableSlots-v.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusConnection.UnregisterMode
        :description: QtDBus/QDBusConnection-UnregisterMode-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.UnregisterMode.UnregisterNode
            :description: QtDBus/QDBusConnection-UnregisterMode-UnregisterNode-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusConnection.UnregisterMode.UnregisterTree
            :description: QtDBus/QDBusConnection-UnregisterMode-UnregisterTree-v.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.__init__
        :args:
            str
        :description: QtDBus/QDBusConnection-__init__-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.__init__
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :description: QtDBus/QDBusConnection-__init__-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.asyncCall
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
            timeout: int = -1
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall`
        :description: QtDBus/QDBusConnection-asyncCall-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.baseService
        :returns:
            str
        :description: QtDBus/QDBusConnection-baseService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.call
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
            mode: :sip:ref:`~PyQt6.QtDBus.QDBus.CallMode` = :sip:ref:`~PyQt6.QtDBus.QDBus.CallMode.Block`
            timeout: int = -1
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusConnection-call-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.callWithCallback
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
            PYQT_SLOT
            PYQT_SLOT
            timeout: int = -1
        :returns:
            bool
        :description: QtDBus/QDBusConnection-callWithCallback-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connect
        :args:
            str
            str
            str
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-connect-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connect
        :args:
            str
            str
            str
            str
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-connect-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connect
        :args:
            str
            str
            str
            str
            Iterable[str]
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-connect-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connectionCapabilities
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection.ConnectionCapabilities`
        :description: QtDBus/QDBusConnection-connectionCapabilities-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connectToBus
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection.BusType`
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :static:
        :description: QtDBus/QDBusConnection-connectToBus-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connectToBus
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :static:
        :description: QtDBus/QDBusConnection-connectToBus-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.connectToPeer
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :static:
        :description: QtDBus/QDBusConnection-connectToPeer-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.disconnect
        :args:
            str
            str
            str
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-disconnect-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.disconnect
        :args:
            str
            str
            str
            str
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-disconnect-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.disconnect
        :args:
            str
            str
            str
            str
            Iterable[str]
            str
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusConnection-disconnect-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.disconnectFromBus
        :args:
            str
        :static:
        :description: QtDBus/QDBusConnection-disconnectFromBus-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.disconnectFromPeer
        :args:
            str
        :static:
        :description: QtDBus/QDBusConnection-disconnectFromPeer-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.interface
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface`
        :description: QtDBus/QDBusConnection-interface-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.isConnected
        :returns:
            bool
        :description: QtDBus/QDBusConnection-isConnected-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.lastError
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusError`
        :description: QtDBus/QDBusConnection-lastError-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.localMachineId
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtDBus/QDBusConnection-localMachineId-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.name
        :returns:
            str
        :description: QtDBus/QDBusConnection-name-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.objectRegisteredAt
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtDBus/QDBusConnection-objectRegisteredAt-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.registerObject
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QObject`
            options: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOptions` = :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAdaptors`
        :returns:
            bool
        :description: QtDBus/QDBusConnection-registerObject-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.registerObject
        :args:
            str
            str
            :sip:ref:`~PyQt6.QtCore.QObject`
            options: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOptions` = :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOptions.ExportAdaptors`
        :returns:
            bool
        :description: QtDBus/QDBusConnection-registerObject-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.registerService
        :args:
            str
        :returns:
            bool
        :description: QtDBus/QDBusConnection-registerService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.send
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :returns:
            bool
        :description: QtDBus/QDBusConnection-send-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.sessionBus
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :static:
        :description: QtDBus/QDBusConnection-sessionBus-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.swap
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :description: QtDBus/QDBusConnection-swap-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.systemBus
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :static:
        :description: QtDBus/QDBusConnection-systemBus-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.unregisterObject
        :args:
            str
            mode: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.UnregisterMode` = :sip:ref:`~PyQt6.QtDBus.QDBusConnection.UnregisterMode.UnregisterNode`
        :description: QtDBus/QDBusConnection-unregisterObject-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusConnection.unregisterService
        :args:
            str
        :returns:
            bool
        :description: QtDBus/QDBusConnection-unregisterService-f.rst

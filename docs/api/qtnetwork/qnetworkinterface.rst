:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkInterface
    :description: QtNetwork/QNetworkInterface-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags
        :description: QtNetwork/QNetworkInterface-InterfaceFlags-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.CanBroadcast
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-CanBroadcast-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.CanMulticast
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-CanMulticast-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.IsLoopBack
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-IsLoopBack-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.IsPointToPoint
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-IsPointToPoint-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.IsRunning
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-IsRunning-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags.IsUp
            :description: QtNetwork/QNetworkInterface-InterfaceFlags-IsUp-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType
        :description: QtNetwork/QNetworkInterface-InterfaceType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.CanBus
            :description: QtNetwork/QNetworkInterface-InterfaceType-CanBus-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ethernet
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ethernet-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Fddi
            :description: QtNetwork/QNetworkInterface-InterfaceType-Fddi-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ieee1394
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ieee1394-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ieee80211
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ieee80211-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ieee802154
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ieee802154-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ieee80216
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ieee80216-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Loopback
            :description: QtNetwork/QNetworkInterface-InterfaceType-Loopback-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Phonet
            :description: QtNetwork/QNetworkInterface-InterfaceType-Phonet-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Ppp
            :description: QtNetwork/QNetworkInterface-InterfaceType-Ppp-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.SixLoWPAN
            :description: QtNetwork/QNetworkInterface-InterfaceType-SixLoWPAN-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Slip
            :description: QtNetwork/QNetworkInterface-InterfaceType-Slip-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Unknown
            :description: QtNetwork/QNetworkInterface-InterfaceType-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Virtual
            :description: QtNetwork/QNetworkInterface-InterfaceType-Virtual-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInterface.InterfaceType.Wifi
            :description: QtNetwork/QNetworkInterface-InterfaceType-Wifi-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.__init__
        :description: QtNetwork/QNetworkInterface-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :description: QtNetwork/QNetworkInterface-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.addressEntries
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`]
        :description: QtNetwork/QNetworkInterface-addressEntries-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.allAddresses
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`]
        :static:
        :description: QtNetwork/QNetworkInterface-allAddresses-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.allInterfaces
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`]
        :static:
        :description: QtNetwork/QNetworkInterface-allInterfaces-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.flags
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.InterfaceFlags`
        :description: QtNetwork/QNetworkInterface-flags-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.hardwareAddress
        :returns:
            str
        :description: QtNetwork/QNetworkInterface-hardwareAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.humanReadableName
        :returns:
            str
        :description: QtNetwork/QNetworkInterface-humanReadableName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.index
        :returns:
            int
        :description: QtNetwork/QNetworkInterface-index-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.interfaceFromIndex
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :static:
        :description: QtNetwork/QNetworkInterface-interfaceFromIndex-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.interfaceFromName
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :static:
        :description: QtNetwork/QNetworkInterface-interfaceFromName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.interfaceIndexFromName
        :args:
            str
        :returns:
            int
        :static:
        :description: QtNetwork/QNetworkInterface-interfaceIndexFromName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.interfaceNameFromIndex
        :args:
            int
        :returns:
            str
        :static:
        :description: QtNetwork/QNetworkInterface-interfaceNameFromIndex-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.isValid
        :returns:
            bool
        :description: QtNetwork/QNetworkInterface-isValid-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.maximumTransmissionUnit
        :returns:
            int
        :description: QtNetwork/QNetworkInterface-maximumTransmissionUnit-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.name
        :returns:
            str
        :description: QtNetwork/QNetworkInterface-name-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :description: QtNetwork/QNetworkInterface-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInterface.type
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.InterfaceType`
        :description: QtNetwork/QNetworkInterface-type-f.rst

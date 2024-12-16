:orphan:

.. sip:class:: PyQt6.QtNetwork.QHostAddress
    :description: QtNetwork/QHostAddress-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag
        :description: QtNetwork/QHostAddress-ConversionModeFlag-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.ConvertLocalHost
            :description: QtNetwork/QHostAddress-ConversionModeFlag-ConvertLocalHost-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.ConvertUnspecifiedAddress
            :description: QtNetwork/QHostAddress-ConversionModeFlag-ConvertUnspecifiedAddress-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.ConvertV4CompatToIPv4
            :description: QtNetwork/QHostAddress-ConversionModeFlag-ConvertV4CompatToIPv4-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.ConvertV4MappedToIPv4
            :description: QtNetwork/QHostAddress-ConversionModeFlag-ConvertV4MappedToIPv4-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.StrictConversion
            :description: QtNetwork/QHostAddress-ConversionModeFlag-StrictConversion-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.TolerantConversion
            :description: QtNetwork/QHostAddress-ConversionModeFlag-TolerantConversion-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QHostAddress.SpecialAddress
        :description: QtNetwork/QHostAddress-SpecialAddress-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any
            :description: QtNetwork/QHostAddress-SpecialAddress-Any-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.AnyIPv4
            :description: QtNetwork/QHostAddress-SpecialAddress-AnyIPv4-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.AnyIPv6
            :description: QtNetwork/QHostAddress-SpecialAddress-AnyIPv6-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.Broadcast
            :description: QtNetwork/QHostAddress-SpecialAddress-Broadcast-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.LocalHost
            :description: QtNetwork/QHostAddress-SpecialAddress-LocalHost-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.LocalHostIPv6
            :description: QtNetwork/QHostAddress-SpecialAddress-LocalHostIPv6-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostAddress.SpecialAddress.Null
            :description: QtNetwork/QHostAddress-SpecialAddress-Null-v.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :description: QtNetwork/QHostAddress-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`
        :description: QtNetwork/QHostAddress-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :args:
            int
        :description: QtNetwork/QHostAddress-__init__-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :args:
            Optional[str]
        :description: QtNetwork/QHostAddress-__init__-f-6.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :args:
            tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int]
        :description: QtNetwork/QHostAddress-__init__-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QHostAddress-__init__-f-5.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.clear
        :description: QtNetwork/QHostAddress-clear-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__eq__
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :returns:
            bool
        :description: QtNetwork/QHostAddress-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`
        :returns:
            bool
        :description: QtNetwork/QHostAddress-__eq__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__hash__
        :returns:
            int
        :description: QtNetwork/QHostAddress-__hash__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isBroadcast
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isBroadcast-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isEqual
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            mode: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.ConversionModeFlag` = :sip:ref:`~PyQt6.QtNetwork.QHostAddress.ConversionModeFlag.TolerantConversion`
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isEqual-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isGlobal
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isGlobal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isInSubnet
        :args:
            tuple[Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`], int]
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isInSubnet-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isInSubnet
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            int
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isInSubnet-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isLinkLocal
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isLinkLocal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isLoopback
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isLoopback-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isMulticast
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isMulticast-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isNull
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isNull-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isPrivateUse
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isPrivateUse-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isSiteLocal
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isSiteLocal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast
        :returns:
            bool
        :description: QtNetwork/QHostAddress-isUniqueLocalUnicast-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__ne__
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :returns:
            bool
        :description: QtNetwork/QHostAddress-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`
        :returns:
            bool
        :description: QtNetwork/QHostAddress-__ne__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.parseSubnet
        :args:
            Optional[str]
        :returns:
            tuple[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, int]
        :static:
        :description: QtNetwork/QHostAddress-parseSubnet-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.protocol
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol`
        :description: QtNetwork/QHostAddress-protocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.scopeId
        :returns:
            str
        :description: QtNetwork/QHostAddress-scopeId-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.setAddress
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`
        :description: QtNetwork/QHostAddress-setAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.setAddress
        :args:
            int
        :description: QtNetwork/QHostAddress-setAddress-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.setAddress
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtNetwork/QHostAddress-setAddress-f-4.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.setAddress
        :args:
            tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int]
        :description: QtNetwork/QHostAddress-setAddress-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.setScopeId
        :args:
            Optional[str]
        :description: QtNetwork/QHostAddress-setScopeId-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QHostAddress-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.toIPv4Address
        :returns:
            int
            bool
        :description: QtNetwork/QHostAddress-toIPv4Address-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.toIPv6Address
        :returns:
            tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int]
        :description: QtNetwork/QHostAddress-toIPv6Address-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostAddress.toString
        :returns:
            str
        :description: QtNetwork/QHostAddress-toString-f.rst

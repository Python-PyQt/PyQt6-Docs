:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkProxy
    :description: QtNetwork/QNetworkProxy-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkProxy.Capability
        :description: QtNetwork/QNetworkProxy-Capability-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.CachingCapability
            :description: QtNetwork/QNetworkProxy-Capability-CachingCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.HostNameLookupCapability
            :description: QtNetwork/QNetworkProxy-Capability-HostNameLookupCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.ListeningCapability
            :description: QtNetwork/QNetworkProxy-Capability-ListeningCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.SctpListeningCapability
            :description: QtNetwork/QNetworkProxy-Capability-SctpListeningCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.SctpTunnelingCapability
            :description: QtNetwork/QNetworkProxy-Capability-SctpTunnelingCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.TunnelingCapability
            :description: QtNetwork/QNetworkProxy-Capability-TunnelingCapability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.Capability.UdpTunnelingCapability
            :description: QtNetwork/QNetworkProxy-Capability-UdpTunnelingCapability-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkProxy.ProxyType
        :description: QtNetwork/QNetworkProxy-ProxyType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy
            :description: QtNetwork/QNetworkProxy-ProxyType-DefaultProxy-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.FtpCachingProxy
            :description: QtNetwork/QNetworkProxy-ProxyType-FtpCachingProxy-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy
            :description: QtNetwork/QNetworkProxy-ProxyType-HttpCachingProxy-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpProxy
            :description: QtNetwork/QNetworkProxy-ProxyType-HttpProxy-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy
            :description: QtNetwork/QNetworkProxy-ProxyType-NoProxy-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkProxy.ProxyType.Socks5Proxy
            :description: QtNetwork/QNetworkProxy-ProxyType-Socks5Proxy-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.__init__
        :description: QtNetwork/QNetworkProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QNetworkProxy-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType`
            hostName: Optional[str] = ''
            port: int = 0
            user: Optional[str] = ''
            password: Optional[str] = ''
        :description: QtNetwork/QNetworkProxy-__init__-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.applicationProxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :static:
        :description: QtNetwork/QNetworkProxy-applicationProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.capabilities
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.Capability`
        :description: QtNetwork/QNetworkProxy-capabilities-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :returns:
            bool
        :description: QtNetwork/QNetworkProxy-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.hasRawHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtNetwork/QNetworkProxy-hasRawHeader-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.header
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`
        :returns:
            Any
        :description: QtNetwork/QNetworkProxy-header-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.hostName
        :returns:
            str
        :description: QtNetwork/QNetworkProxy-hostName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.isCachingProxy
        :returns:
            bool
        :description: QtNetwork/QNetworkProxy-isCachingProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.isTransparentProxy
        :returns:
            bool
        :description: QtNetwork/QNetworkProxy-isTransparentProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :returns:
            bool
        :description: QtNetwork/QNetworkProxy-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.password
        :returns:
            str
        :description: QtNetwork/QNetworkProxy-password-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.port
        :returns:
            int
        :description: QtNetwork/QNetworkProxy-port-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.rawHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkProxy-rawHeader-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.rawHeaderList
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetwork/QNetworkProxy-rawHeaderList-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setApplicationProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :static:
        :description: QtNetwork/QNetworkProxy-setApplicationProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setCapabilities
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.Capability`
        :description: QtNetwork/QNetworkProxy-setCapabilities-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setHeader
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`
            Any
        :description: QtNetwork/QNetworkProxy-setHeader-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setHostName
        :args:
            Optional[str]
        :description: QtNetwork/QNetworkProxy-setHostName-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setPassword
        :args:
            Optional[str]
        :description: QtNetwork/QNetworkProxy-setPassword-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setPort
        :args:
            int
        :description: QtNetwork/QNetworkProxy-setPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setRawHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNetwork/QNetworkProxy-setRawHeader-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setType
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType`
        :description: QtNetwork/QNetworkProxy-setType-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.setUser
        :args:
            Optional[str]
        :description: QtNetwork/QNetworkProxy-setUser-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QNetworkProxy-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.type
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType`
        :description: QtNetwork/QNetworkProxy-type-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkProxy.user
        :returns:
            str
        :description: QtNetwork/QNetworkProxy-user-f.rst

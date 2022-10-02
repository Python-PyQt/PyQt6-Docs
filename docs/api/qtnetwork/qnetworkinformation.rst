:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkInformation
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QNetworkInformation-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInformation.Feature
        :description: QtNetwork/QNetworkInformation-Feature-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.CaptivePortal
            :description: QtNetwork/QNetworkInformation-Feature-CaptivePortal-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.Metered
            :description: QtNetwork/QNetworkInformation-Feature-Metered-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.Reachability
            :description: QtNetwork/QNetworkInformation-Feature-Reachability-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.TransportMedium
            :description: QtNetwork/QNetworkInformation-Feature-TransportMedium-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInformation.Reachability
        :description: QtNetwork/QNetworkInformation-Reachability-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Reachability.Disconnected
            :description: QtNetwork/QNetworkInformation-Reachability-Disconnected-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Reachability.Local
            :description: QtNetwork/QNetworkInformation-Reachability-Local-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Reachability.Online
            :description: QtNetwork/QNetworkInformation-Reachability-Online-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Reachability.Site
            :description: QtNetwork/QNetworkInformation-Reachability-Site-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Reachability.Unknown
            :description: QtNetwork/QNetworkInformation-Reachability-Unknown-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium
        :description: QtNetwork/QNetworkInformation-TransportMedium-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium.Bluetooth
            :description: QtNetwork/QNetworkInformation-TransportMedium-Bluetooth-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium.Cellular
            :description: QtNetwork/QNetworkInformation-TransportMedium-Cellular-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium.Ethernet
            :description: QtNetwork/QNetworkInformation-TransportMedium-Ethernet-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium.Unknown
            :description: QtNetwork/QNetworkInformation-TransportMedium-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.TransportMedium.WiFi
            :description: QtNetwork/QNetworkInformation-TransportMedium-WiFi-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.availableBackends
        :returns:
            List[str]
        :static:
        :description: QtNetwork/QNetworkInformation-availableBackends-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.backendName
        :returns:
            str
        :description: QtNetwork/QNetworkInformation-backendName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.instance
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation`
        :static:
        :description: QtNetwork/QNetworkInformation-instance-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.isBehindCaptivePortal
        :returns:
            bool
        :description: QtNetwork/QNetworkInformation-isBehindCaptivePortal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.isMetered
        :returns:
            bool
        :description: QtNetwork/QNetworkInformation-isMetered-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.load
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtNetwork/QNetworkInformation-load-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.load
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`
        :returns:
            bool
        :static:
        :description: QtNetwork/QNetworkInformation-load-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.loadBackendByFeatures
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`
        :returns:
            bool
        :static:
        :description: QtNetwork/QNetworkInformation-loadBackendByFeatures-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.loadBackendByName
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtNetwork/QNetworkInformation-loadBackendByName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.loadDefaultBackend
        :returns:
            bool
        :static:
        :description: QtNetwork/QNetworkInformation-loadDefaultBackend-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.reachability
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability`
        :description: QtNetwork/QNetworkInformation-reachability-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.supportedFeatures
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`
        :description: QtNetwork/QNetworkInformation-supportedFeatures-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.supports
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`
        :returns:
            bool
        :description: QtNetwork/QNetworkInformation-supports-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.transportMedium
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.TransportMedium`
        :description: QtNetwork/QNetworkInformation-transportMedium-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.isBehindCaptivePortalChanged
        :args:
            bool
        :description: QtNetwork/QNetworkInformation-isBehindCaptivePortalChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.isMeteredChanged
        :args:
            bool
        :description: QtNetwork/QNetworkInformation-isMeteredChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.reachabilityChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability`
        :description: QtNetwork/QNetworkInformation-reachabilityChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.transportMediumChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.TransportMedium`
        :description: QtNetwork/QNetworkInformation-transportMediumChanged-s.rst

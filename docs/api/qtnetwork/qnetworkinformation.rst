:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkInformation
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QNetworkInformation-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkInformation.Feature
        :description: QtNetwork/QNetworkInformation-Feature-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.CaptivePortal
            :description: QtNetwork/QNetworkInformation-Feature-CaptivePortal-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkInformation.Feature.Reachability
            :description: QtNetwork/QNetworkInformation-Feature-Reachability-v.rst

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

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.reachability
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability`
        :description: QtNetwork/QNetworkInformation-reachability-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkInformation.supports
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`
        :returns:
            bool
        :description: QtNetwork/QNetworkInformation-supports-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.isBehindCaptivePortalChanged
        :args:
            bool
        :description: QtNetwork/QNetworkInformation-isBehindCaptivePortalChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkInformation.reachabilityChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability`
        :description: QtNetwork/QNetworkInformation-reachabilityChanged-s.rst

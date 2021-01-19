:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkAddressEntry
    :description: QtNetwork/QNetworkAddressEntry-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus
        :description: QtNetwork/QNetworkAddressEntry-DnsEligibilityStatus-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsEligibilityUnknown
            :description: QtNetwork/QNetworkAddressEntry-DnsEligibilityStatus-DnsEligibilityUnknown-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsEligible
            :description: QtNetwork/QNetworkAddressEntry-DnsEligibilityStatus-DnsEligible-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsIneligible
            :description: QtNetwork/QNetworkAddressEntry-DnsEligibilityStatus-DnsIneligible-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.__init__
        :description: QtNetwork/QNetworkAddressEntry-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`
        :description: QtNetwork/QNetworkAddressEntry-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.broadcast
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QNetworkAddressEntry-broadcast-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.clearAddressLifetime
        :description: QtNetwork/QNetworkAddressEntry-clearAddressLifetime-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.dnsEligibility
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus`
        :description: QtNetwork/QNetworkAddressEntry-dnsEligibility-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`
        :returns:
            bool
        :description: QtNetwork/QNetworkAddressEntry-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.ip
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QNetworkAddressEntry-ip-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown
        :returns:
            bool
        :description: QtNetwork/QNetworkAddressEntry-isLifetimeKnown-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.isPermanent
        :returns:
            bool
        :description: QtNetwork/QNetworkAddressEntry-isPermanent-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.isTemporary
        :returns:
            bool
        :description: QtNetwork/QNetworkAddressEntry-isTemporary-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`
        :returns:
            bool
        :description: QtNetwork/QNetworkAddressEntry-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.netmask
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QNetworkAddressEntry-netmask-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.preferredLifetime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`
        :description: QtNetwork/QNetworkAddressEntry-preferredLifetime-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.prefixLength
        :returns:
            int
        :description: QtNetwork/QNetworkAddressEntry-prefixLength-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setAddressLifetime
        :args:
            :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`
            :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`
        :description: QtNetwork/QNetworkAddressEntry-setAddressLifetime-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setBroadcast
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QNetworkAddressEntry-setBroadcast-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setDnsEligibility
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus`
        :description: QtNetwork/QNetworkAddressEntry-setDnsEligibility-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setIp
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QNetworkAddressEntry-setIp-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setNetmask
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QNetworkAddressEntry-setNetmask-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.setPrefixLength
        :args:
            int
        :description: QtNetwork/QNetworkAddressEntry-setPrefixLength-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`
        :description: QtNetwork/QNetworkAddressEntry-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAddressEntry.validityLifetime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`
        :description: QtNetwork/QNetworkAddressEntry-validityLifetime-f.rst

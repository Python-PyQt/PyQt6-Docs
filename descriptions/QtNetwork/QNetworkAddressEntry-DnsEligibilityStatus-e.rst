.. sip:enum-description::
    :status: todo
    :digest: d3609ec7abbb2ccfa95ca08f0cc0da2b

This enum indicates whether a given host address is eligible to be published in the Domain Name System (DNS) or other similar name resolution mechanisms. In general, an address is suitable for publication if it is an address this machine will be reached at for an indeterminate amount of time, though it need not be permanent. For example, addresses obtained via DHCP are often eligible, but cryptographically-generated temporary IPv6 addresses are not.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.dnsEligibility`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setDnsEligibility`.

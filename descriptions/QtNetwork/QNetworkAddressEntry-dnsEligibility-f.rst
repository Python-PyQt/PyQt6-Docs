.. sip:method-description::
    :status: todo
    :pysig: 90b2e6a8708266360bac6d31513f1f15
    :realsig: () const
    :digest: e58965914764203585ed647cd4ff0ee9

Returns whether this address is eligible for publication in the Domain Name System (DNS) or similar name resolution mechanisms.

In general, an address is suitable for publication if it is an address this machine will be reached at for an indeterminate amount of time, though it need not be permanent. For example, addresses obtained via DHCP are often eligible, but cryptographically-generated temporary IPv6 addresses are not.

On some systems, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` will need to heuristically determine which addresses are eligible.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isPermanent`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setDnsEligibility`.

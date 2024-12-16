.. sip:method-description::
    :status: todo
    :pysig: a9bb3cdd730e6b72fdc0b732361dcf79
    :realsig: (const QHostAddress&, quint16)
    :digest: b8abe4979442d3c3432672d8b62ff4d9

Sets the nameserver to *nameserver* and the port to *port*.

**Note:** Setting the port number to any value other than the default (53) can cause the name resolution to fail, depending on the operating system limitations and firewalls, if the :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserverProtocol` to be used :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Protocol.Standard`. Notably, the Windows API used by :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` is unable to handle alternate port numbers.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserver`, :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserverPort`.

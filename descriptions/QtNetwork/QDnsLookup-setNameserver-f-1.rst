.. sip:method-description::
    :status: todo
    :pysig: a9bb3cdd730e6b72fdc0b732361dcf79
    :realsig: (const QHostAddress&, quint16)
    :digest: 1f4dbaf095fc7ebd12bdf295695b92cf

Sets the nameserver to *nameserver* and the port to *port*.

**Note:** Setting the port number to any value other than the default (53) can cause the name resolution to fail, depending on the operating system limitations and firewalls. Notably, the Windows API used by :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` is unable to handle alternate port numbers.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserver`, :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserverPort`.

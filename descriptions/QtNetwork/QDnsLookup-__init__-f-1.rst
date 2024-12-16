.. sip:method-description::
    :status: todo
    :pysig: 6730cdea6e53155cdcc4cafdccb74010
    :realsig: (QDnsLookup::Type, const QString&, QDnsLookup::Protocol, const QHostAddress&, quint16, QObject*)
    :digest: 0f21ac615b1cdb6afe18cc28daa79013

Constructs a :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` object to issue a query for *name* of record type *type*, using the DNS server *nameserver* running on port *port*, and sets *parent* as the parent object.

The query will be sent using *protocol*, if supported. Use :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.isProtocolSupported` to check if it is supported.

**Note:** Setting the port number to any value other than the default (53) can cause the name resolution to fail, depending on the operating system limitations and firewalls, if the :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserverProtocol` to be used :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Protocol.Standard`. Notably, the Windows API used by :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` is unable to handle alternate port numbers.

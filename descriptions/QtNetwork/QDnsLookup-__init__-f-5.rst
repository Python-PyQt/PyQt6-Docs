.. sip:method-description::
    :status: todo
    :pysig: f5f7ae1675c1ede00116830dc7a0d169
    :realsig: (QDnsLookup::Type, const QString&, const QHostAddress&, quint16, QObject*)
    :digest: feddfdf9344a6839ddc8a1c642ae2759

Constructs a :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` object to issue a query for *name* of record type *type*, using the DNS server *nameserver* running on port *port*, and sets *parent* as the parent object.

**Note:** Setting the port number to any value other than the default (53) can cause the name resolution to fail, depending on the operating system limitations and firewalls, if the :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.nameserverProtocol` to be used :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Protocol.Standard`. Notably, the Windows API used by :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` is unable to handle alternate port numbers.

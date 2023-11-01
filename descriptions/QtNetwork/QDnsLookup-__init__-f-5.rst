.. sip:method-description::
    :status: todo
    :pysig: f5f7ae1675c1ede00116830dc7a0d169
    :realsig: (QDnsLookup::Type, const QString&, const QHostAddress&, quint16, QObject*)
    :digest: 6b7315a823ff01b75bd2afba27746018

Constructs a :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` object to issue a query for *name* of record type *type*, using the DNS server *nameserver* running on port *port*, and sets *parent* as the parent object.

**Note:** Setting the port number to any value other than the default (53) can cause the name resolution to fail, depending on the operating system limitations and firewalls. Notably, the Windows API used by :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` is unable to handle alternate port numbers.

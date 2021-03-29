.. sip:class-description::
    :status: todo
    :brief: Represents a DNS lookup
    :digest: a189790dca1ab84a5090f885eeed571b

The :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` class represents a DNS lookup.

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` uses the mechanisms provided by the operating system to perform DNS lookups. To perform a lookup you need to specify a :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.name` and :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.type` then invoke the :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.lookup` slot. The :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.finished` signal will be emitted upon completion.

For example, you can determine which servers an XMPP chat client should connect to for a given domain with:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qdnslookup.py
    :lines: 54-65

Once the request finishes you can handle the results with:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qdnslookup.py
    :lines: 70-85

**Note:** If you simply want to find the IP address(es) associated with a host name, or the host name associated with an IP address you should use :sip:ref:`~PyQt6.QtNetwork.QHostInfo` instead.

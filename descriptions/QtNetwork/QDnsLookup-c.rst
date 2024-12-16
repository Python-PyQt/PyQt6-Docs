.. sip:class-description::
    :status: todo
    :brief: Represents a DNS lookup
    :digest: 8671506b868035212a15952b0bc35bed

The :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` class represents a DNS lookup.

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` uses the mechanisms provided by the operating system to perform DNS lookups. To perform a lookup you need to specify a :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.name` and :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.type` then invoke the :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.lookup` slot. The :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.finished` signal will be emitted upon completion.

For example, you can determine which servers an XMPP chat client should connect to for a given domain with:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qdnslookup.py
    :lines: 54-65

Once the request finishes you can handle the results with:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qdnslookup.py
    :lines: 70-85

**Note:** If you simply want to find the IP address(es) associated with a host name, or the host name associated with an IP address you should use :sip:ref:`~PyQt6.QtNetwork.QHostInfo` instead.

.. _qdnslookup-dns-over-tls-and-authentic-data:

DNS-over-TLS and Authentic Data
-------------------------------

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` supports DNS-over-TLS (DoT, as specified by RFC 7858) on some platforms. That currently includes all Unix platforms where regular queries are supported, if :sip:ref:`~PyQt6.QtNetwork.QSslSocket` support is present in Qt. To query if support is present at runtime, use :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.isProtocolSupported`.

When using DNS-over-TLS, :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` only implements the "Opportunistic Privacy Profile" method of authentication, as described in RFC 7858 section 4.1. In this mode, :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` (through :sip:ref:`~PyQt6.QtNetwork.QSslSocket`) only validates that the server presents a certificate that is valid for the server being connected to. Clients may use :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.setSslConfiguration` to impose additional restrictions and :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.sslConfiguration` to obtain information after the query is complete.

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` will request DNS servers queried over TLS to perform authentication on the data they return. If they confirm the data is valid, the authenticData property will be set to true. :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` does not verify the integrity of the data by itself, so applications should only trust this property on servers they have confirmed through other means to be trustworthy.

.. _qdnslookup-authentic-data-without-tls:

Authentic Data without TLS
..........................

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` request Authentic Data for any server set with :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.setNameserver`, even if TLS encryption is not required. This is useful when querying a caching nameserver on the same host as the application or on a trusted network. Though similar to the TLS case, the application is responsible for determining if the server it chose to use is trustworthy, and if the unencrypted connection cannot be tampered with.

:sip:ref:`~PyQt6.QtNetwork.QDnsLookup` obeys the system configuration to request Authentic Data on the default nameserver (that is, if :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.setNameserver` is not called). This is currently only supported on Linux systems using glibc 2.31 or later. On any other systems, :sip:ref:`~PyQt6.QtNetwork.QDnsLookup` will ignore the AD bit in the query header.

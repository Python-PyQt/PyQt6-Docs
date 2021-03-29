.. sip:class-description::
    :status: todo
    :brief: Static functions for host name lookups
    :digest: 876eaca2386ff64bc838ef2765581e93

The :sip:ref:`~PyQt6.QtNetwork.QHostInfo` class provides static functions for host name lookups.

:sip:ref:`~PyQt6.QtNetwork.QHostInfo` finds the IP address(es) associated with a host name, or the host name associated with an IP address. The class provides two static convenience functions: one that works asynchronously and emits a signal once the host is found, and one that blocks and returns a :sip:ref:`~PyQt6.QtNetwork.QHostInfo` object.

To look up a host's IP addresses asynchronously, call :sip:ref:`~PyQt6.QtNetwork.QHostInfo.lookupHost`, which takes the host name or IP address, a receiver object, and a slot signature as arguments and returns an ID. You can abort the lookup by calling :sip:ref:`~PyQt6.QtNetwork.QHostInfo.abortHostLookup` with the lookup ID.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qhostinfo.py
    :lines: 54-60

The slot is invoked when the results are ready. The results are stored in a :sip:ref:`~PyQt6.QtNetwork.QHostInfo` object. Call :sip:ref:`~PyQt6.QtNetwork.QHostInfo.addresses` to get the list of IP addresses for the host, and :sip:ref:`~PyQt6.QtNetwork.QHostInfo.hostName` to get the host name that was looked up.

If the lookup failed, :sip:ref:`~PyQt6.QtNetwork.QHostInfo.error` returns the type of error that occurred. :sip:ref:`~PyQt6.QtNetwork.QHostInfo.errorString` gives a human-readable description of the lookup error.

If you want a blocking lookup, use the :sip:ref:`~PyQt6.QtNetwork.QHostInfo.fromName` function:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qhostinfo.py
    :lines: 65-65

:sip:ref:`~PyQt6.QtNetwork.QHostInfo` supports Internationalized Domain Names (IDNs) through the IDNA and Punycode standards.

To retrieve the name of the local host, use the static :sip:ref:`~PyQt6.QtNetwork.QHostInfo.localHostName` function.

:sip:ref:`~PyQt6.QtNetwork.QHostInfo` uses the mechanisms provided by the operating system to perform the lookup. As per {https://tools.ietf.org/html/rfc6724}{RFC 6724} there is no guarantee that all IP addresses registered for a domain or host will be returned.

**Note:** Since Qt 4.6.1 :sip:ref:`~PyQt6.QtNetwork.QHostInfo` is using multiple threads for DNS lookup instead of one dedicated DNS thread. This improves performance, but also changes the order of signal emissions when using :sip:ref:`~PyQt6.QtNetwork.QHostInfo.lookupHost` compared to previous versions of Qt.

**Note:** Since Qt 4.6.3 :sip:ref:`~PyQt6.QtNetwork.QHostInfo` is using a small internal 60 second DNS cache for performance improvements.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`, `RFC 3492 <http://www.rfc-editor.org/rfc/rfc3492.txt>`_, `RFC 6724 <https://tools.ietf.org/html/rfc6724>`_.

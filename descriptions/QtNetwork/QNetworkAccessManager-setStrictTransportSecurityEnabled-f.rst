.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: a58cc26fbd2460aaaeeccff2edbb2d65

If *enabled* is ``true``, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` follows the HTTP Strict Transport Security policy (HSTS, RFC6797). When processing a request, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` automatically replaces the "http" scheme with "https" and uses a secure transport for HSTS hosts. If it's set explicitly, port 80 is replaced by port 443.

When HSTS is enabled, for each HTTP response containing HSTS header and received over a secure transport, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will update its HSTS cache, either remembering a host with a valid policy or removing a host with an expired or disabled HSTS policy.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.isStrictTransportSecurityEnabled`.

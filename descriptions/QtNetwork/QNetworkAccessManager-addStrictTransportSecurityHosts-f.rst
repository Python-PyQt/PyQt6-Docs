.. sip:method-description::
    :status: todo
    :pysig: 421c92123dec64bf6004ea8c0533e32a
    :realsig: (const QList<QHstsPolicy>&)
    :digest: 74bfaae439157d845b6b94f585f5147b

Adds HTTP Strict Transport Security policies into HSTS cache. *knownHosts* contains the known hosts that have :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy` information.

**Note:** An expired policy will remove a known host from the cache, if previously present.

**Note:** While processing HTTP responses, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` can also update the HSTS cache, removing or updating exitsting policies or introducing new *knownHosts*. The current implementation thus is server-driven, client code can provide :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` with previously known or discovered policies, but this information can be overridden by "Strict-Transport-Security" response headers.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.strictTransportSecurityHosts`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.enableStrictTransportSecurityStore`, :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy`.

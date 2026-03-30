.. sip:method-description::
    :status: todo
    :pysig: 4d97b018bee63412c50592ec6cafcf35
    :realsig: (const QString&)
    :digest: 5b129f74340c4a1ce370703df28be157

If a backend with name *backendName* is available, this function returns the list of TLS protocol versions supported by this backend. An empty *backendName* is understood as a query about the currently active backend. Otherwise, this function returns an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.availableBackends`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.activeBackend`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.isProtocolSupported`.

.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 2a7c8f449d32833fe2a07b34bead6d62

Returns true if a backend with name *backendName* was set as active backend. *backendName* must be one of names returned by :sip:ref:`~PyQt6.QtNetwork.QSslSocket.availableBackends`.

**Note:** An application cannot mix different backends simultaneously. This implies that a non-default backend must be selected prior to any use of :sip:ref:`~PyQt6.QtNetwork.QSslSocket` or related classes, e.g. :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` or :sip:ref:`~PyQt6.QtNetwork.QSslKey`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.activeBackend`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.availableBackends`.

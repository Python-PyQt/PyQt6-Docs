.. sip:signal-description::
    :status: todo
    :pysig: fbdd6f620cf8365525ff0af7091116a0
    :realsig: (QWebEngineClientCertificateSelection)
    :digest: 2247d1cf7f8d6dee36a999359dcebf72

This signal is emitted when a web site requests an SSL client certificate, and one or more were found in system's client certificate store.

Handling the signal is asynchronous, and loading will be waiting until a certificate is selected, or the last copy of *clientCertificateSelection* is destroyed.

If the signal is not handled, *clientCertificateSelection* is automatically destroyed, and loading will continue without a client certificate.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientCertificateSelection`.

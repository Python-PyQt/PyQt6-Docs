.. sip:class-description::
    :status: todo
    :brief: QWebEngineClientCertSelection class wraps a client certificate selection
    :digest: 14b8f1e0d051e3e0ffcc43d53dae46e5

The QWebEngineClientCertSelection class wraps a client certificate selection.

When a web site requests an SSL client certificate, and one or more certificates are found in the system's client certificate store, this class provides access to the certificates to choose from, as well as a method for selecting one.

The selection is asynchronous. If no certificate is selected and no copy of the object is kept alive, loading will continue without a certificate.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.selectClientCertificate`.

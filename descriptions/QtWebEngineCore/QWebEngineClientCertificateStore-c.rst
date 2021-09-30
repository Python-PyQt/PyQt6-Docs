.. sip:class-description::
    :status: todo
    :brief: In-memory store for client certificates
    :digest: ba551a7dfa89b82f7459ec3822f34277

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientCertificateStore` class provides an in-memory store for client certificates.

The class allows to store client certificates in an in-memory store. When a web site requests an SSL client certificate, the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.selectClientCertificate` signal is emitted with matching certificates from the native certificate store or the in-memory store. The getInstance() method can be used to access the single instance of the class.

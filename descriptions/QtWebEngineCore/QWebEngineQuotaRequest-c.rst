.. sip:class-description::
    :status: todo
    :brief: Enables accepting or rejecting requests for larger persistent storage than the application's current allocation in File System API
    :digest: 33cd0acdd6434e5c66d294a2ac85f0b8

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineQuotaRequest` class enables accepting or rejecting requests for larger persistent storage than the application's current allocation in File System API.

This class is used by the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.quotaRequested` signal to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineQuotaRequest.accept` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineQuotaRequest.reject` a request for an increase in the persistent storage allocated to the application. The default quota is 0 bytes.

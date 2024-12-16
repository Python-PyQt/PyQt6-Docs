.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 55eb2e0af7c0900ad301d8e8d2b895d0

A request will be made only the first time a permission is needed. Any subsequent requests will be automatically granted or denied, depending on the initial user choice. This carries over to all pages that use the same :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` instance, until the application is shut down. This is the setting applied if ``off-the-record`` is set or no persistent data path is available.

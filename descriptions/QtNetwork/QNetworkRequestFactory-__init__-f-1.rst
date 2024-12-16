.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: b798e91ca714412bb141af81a0f82d4e

Creates a new :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory` object, initializing the base URL to *baseUrl*. The base URL is used to populate subsequent network requests.

If the URL contains a *path* component, it will be extracted and used as a base path in subsequent network requests. This means that any paths provided when requesting individual requests will be appended to this base path, as illustrated below:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkrequestfactory.py
    :lines: 22-27

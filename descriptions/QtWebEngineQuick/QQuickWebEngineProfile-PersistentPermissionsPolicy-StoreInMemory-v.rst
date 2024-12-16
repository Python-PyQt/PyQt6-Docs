.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 13966201ae444828d304b4eff9780fcf

A request will be made only the first time a permission is needed. Any subsequent requests will be automatically granted or denied, depending on the initial user choice. This carries over to all pages that use the same :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile` instance, until the application is shut down. This is the setting applied if ``off-the-record`` is set or no persistent data path is available.

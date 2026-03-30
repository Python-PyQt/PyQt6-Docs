.. sip:enum-member-description::
    :status: todo
    :value: 28
    :digest: 3045c5bf631028816d2cdb948386b9a0

Enables JavaScript ``execCommand("paste")``. This also requires enabling JavascriptCanAccessClipboard. Since unrestricted clipboard access is a potential security concern, it is recommended that applications leave this disabled and instead respond to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.Feature.ClipboardReadWrite` feature permission requests. Disabled by default.

.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: b505e8074496c3a4035e54839bf781ad

Allows JavaScript programs to write (copy) sanitized content to the clipboard. A sanitized write is done with the ``write`` and ``writeText`` JavaScript Clipboard API calls and must be accompanied by user action. Unsanitized writes, and reading from the clipboard, are enabled by JavascriptCanPaste. Prior to Chromium version 81, this setting enabled all clipboard writes. Since unrestricted clipboard access is a potential security concern, it is recommended that applications leave this disabled and instead respond to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.Feature.ClipboardReadWrite` feature permission requests. Disabled by default.

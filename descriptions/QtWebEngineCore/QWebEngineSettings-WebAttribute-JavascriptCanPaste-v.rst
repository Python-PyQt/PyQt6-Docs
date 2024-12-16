.. sip:enum-member-description::
    :status: todo
    :value: 28
    :digest: 2e5d3a106cc1c6fdf2b168d131d815e9

Allows JavaScript programs to read (paste) from the clipboard and to write unsanitized content. A sanitized write is done with the ``write`` and ``writeText`` JavaScript Clipboard API calls and must be accompanied by user action; unsanitized writes are any writes which do not meet these criteria. For this setting to have any effect, JavascriptCanAccessClipboard must also be enabled. Since unrestricted clipboard access is a potential security concern, it is recommended that applications leave this disabled and instead respond to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.Feature.ClipboardReadWrite` feature permission requests. Disabled by default. (Added in Qt 5.11)

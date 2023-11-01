.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: dcc69e6af004768302761cbdc3cd074d

Enable DNS-over-HTTPS and only allow hosts to be resolved this way. DoH servers have to be provided through serverTemplates in the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineGlobalSettings.DnsMode` structure. If the DNS-over-HTTPS resolution fails, there is no fallback and the DNS host resolution fails completely.

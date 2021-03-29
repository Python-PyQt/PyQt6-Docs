.. sip:enum-member-description::
    :status: todo
    :value: 23
    :digest: 6ac28026642dfa1009c00f7a90702503

Requests only, type: :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Bool` (default: false) If set, this attribute will force :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` to use HTTP/2 protocol without initial HTTP/2 protocol negotiation. Use of this attribute implies prior knowledge that a particular server supports HTTP/2. The attribute works with SSL or 'cleartext' HTTP/2. If a server turns out to not support HTTP/2, when HTTP/2 direct was specified, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` gives up, without attempting to fall back to HTTP/1.1. If both  and  are set,  takes priority. (This value was introduced in 5.11.)

.. sip:enum-member-description::
    :status: todo
    :value: 29
    :digest: eb30fb23d1f154757de002b98097878b

Requests only, type: QMetaType::String Holds the full local server name to be used for the underlying :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`. This attribute is used by the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` to connect to a specific local server, when :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`'s behavior for a simple name isn't enough. The URL in the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest` must still use unix+http: or local+http: scheme. And the hostname in the URL will be used for the Host header in the HTTP request. (This value was introduced in 6.8.)

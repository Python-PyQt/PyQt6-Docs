.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 2751e00a855b6f39c1a16846929b4f89

Replies only, type: :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QUrl` (no default) If present, it indicates that the server is redirecting the request to a different URL. The Network Access API does follow redirections by default, but if :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.ManualRedirectPolicy` is enabled and the redirect was not handled in redirected() then this attribute will be present. The returned URL might be relative. Use :sip:ref:`~PyQt6.QtCore.QUrl.resolved` to create an absolute URL out of it.

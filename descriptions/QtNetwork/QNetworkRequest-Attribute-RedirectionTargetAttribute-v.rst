.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: fe1baa23132dc289e4be5123e55d0288

Replies only, type: :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QUrl` (no default) If present, it indicates that the server is redirecting the request to a different URL. The Network Access API does follow redirections by default, unless :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.ManualRedirectPolicy` is used. Additionally, if :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.UserVerifiedRedirectPolicy` is used, then this attribute will be set if the redirect was not followed. The returned URL might be relative. Use :sip:ref:`~PyQt6.QtCore.QUrl.resolved` to create an absolute URL out of it.

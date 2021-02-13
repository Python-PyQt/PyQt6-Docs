.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: bbf4825eba465fc480c23c915d2766d3

Client decides whether to follow each redirect by handling the redirected() signal, emitting redirectAllowed() on the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object to allow the redirect or aborting/finishing it to reject the redirect. This can be used, for example, to ask the user whether to accept the redirect, or to decide based on some app-specific configuration.

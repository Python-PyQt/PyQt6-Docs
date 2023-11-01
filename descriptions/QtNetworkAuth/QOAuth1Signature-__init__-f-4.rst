.. sip:method-description::
    :status: todo
    :pysig: e3287cf23e7c6776f4d70fdc53922cd4
    :realsig: (const QUrl&, const QString&, const QString&, QOAuth1Signature::HttpRequestMethod, const QMultiMap<QString, QVariant>&)
    :digest: 61625505856e3485c1ec86c9e1cd030c

Creates a :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature` using

* *url* as the target address

* *clientSharedKey* as the user token used to verify the signature

* *tokenSecret* as the negotiated token used to verify the signature

* *method* as the HTTP method used to send the request

* and the given user *parameters* to augment the request.

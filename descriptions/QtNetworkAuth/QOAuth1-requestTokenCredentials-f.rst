.. sip:method-description::
    :status: todo
    :pysig: 2285a78e45339995a88e0e97b3d2edac
    :realsig: (QNetworkAccessManager::Operation, const QUrl&, const std::pair<QString, QString>&, const QVariantMap&)
    :digest: d7a14a0cc2d6f8bb48fb690d07d93a71

Starts a request for token credentials using the request method *operation*. The request URL is *url* and the *parameters* shall be encoded and sent during the request. The *temporaryToken* pair of string is used to identify and sign the request.

**See also**: `The OAuth 1.0 Protocol: Token Credentials <https://tools.ietf.org/html/rfc5849#section-2.3>`_

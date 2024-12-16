.. sip:enum-description::
    :status: todo
    :digest: fcbbcb45dc7f1a869a2acf3542e76306

List of available `Proof Key for Code Exchange (PKCE) methods <https://datatracker.ietf.org/doc/html/rfc7636>`_.

PKCE is a security measure to mitigate the risk of `authorization code interception attacks <https://datatracker.ietf.org/doc/html/rfc7636#section-1>`_. As such it is relevant for OAuth2 "Authorization Code" flow (grant) and in particular with native applications.

PKCE inserts additional parameters into authorization and access token requests. With the help of these parameters the authorization server is able to verify that an access token request originates from the same entity that issued the authorization request.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.setPkceMethod`, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.pkceMethod`.

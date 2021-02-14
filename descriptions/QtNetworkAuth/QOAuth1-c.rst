.. sip:class-description::
    :status: todo
    :brief: Implementation of the OAuth 1 Protocol
    :digest: c5875a3b9432309bcef375a3a3f03c46

The :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1` class provides an implementation of the `OAuth 1 Protocol <https://tools.ietf.org/html/rfc5849>`_.

:sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1` provides a method for clients to access server resources on behalf of a resource owner (such as a different client or an end-user). It also provides a process for end-users to authorize third-party access to their server resources without sharing their credentials (typically, a username and password pair), using user-agent redirections.

:sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1` uses tokens to represent the authorization granted to the client by the resource owner. Typically, token credentials are issued by the server at the resource owner's request, after authenticating the resource owner's identity (usually using a username and password).

When making the temporary credentials request, the client authenticates using only the client credentials. When making the token request, the client authenticates using the client credentials as well as the temporary credentials. Once the client receives and stores the token credentials, it can proceed to access protected resources on behalf of the resource owner by making authenticated requests using the client credentials together with the token credentials received.

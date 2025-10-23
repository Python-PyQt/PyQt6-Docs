.. sip:class-description::
    :status: todo
    :brief: Implementation of the Authorization Code Grant flow
    :digest: 56a883c8a8eb95569f2c5a50ca67e364

The :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow` class provides an implementation of the `Authorization Code Grant <https://tools.ietf.org/html/rfc6749#section-4.1>`_ flow.

This class implements the `Authorization Code Grant <https://tools.ietf.org/html/rfc6749#section-4.1>`_ flow, which is used both to obtain and to refresh access tokens. It is a redirection-based flow so the user will need access to a web browser.

As a redirection-based flow this class requires a proper reply handler to be set. See `OAuth 2.0 Overview <https://doc.qt.io/qt-6/qt-oauth2-overview.html>`_, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthHttpServerReplyHandler`, and :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler`.

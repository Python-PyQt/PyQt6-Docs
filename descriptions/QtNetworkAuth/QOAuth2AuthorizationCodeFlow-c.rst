.. sip:class-description::
    :status: todo
    :brief: Implementation of the Authorization Code Grant flow
    :digest: f509cc6b7011eb4f22e71d2c4a3f55f4

The :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow` class provides an implementation of the `Authorization Code Grant <https://tools.ietf.org/html/rfc6749#section-4.1>`_ flow.

This class implements the `Authorization Code Grant <https://tools.ietf.org/html/rfc6749#section-4.1>`_ flow, which is used both to obtain and to refresh access tokens. It is a redirection-based flow so the user will need access to a web browser.

As a redirection-based flow this class requires a proper reply handler to be set. See `Qt OAuth2 Overview <https://doc.qt.io/qt-6/qt-oauth2-overview.html>`_, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthHttpServerReplyHandler`, and :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler`.

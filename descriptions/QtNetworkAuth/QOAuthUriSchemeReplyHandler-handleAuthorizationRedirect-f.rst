.. sip:method-description::
    :status: todo
    :pysig: 690ff780a2b2b089099cc8704f4803c0
    :realsig: (const QUrl&)
    :digest: 5df6da7ccb77f972901e335dbf5404fd

This function is used to supply the redirect URL the Authorization Server provides at the end of the authorization stage. The provided *url* undergoes the same URL matching as described in :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler.redirectUrl`.

Suppyling the URL can be useful for scenarios where this redirect URL is captured by some other means, for example with `Qt WebEngine <https://doc.qt.io/qt-6/qtwebengine-index.html>`_ or through some other custom arrangement. This way such agent usage can be integrated with rest of the OAuth2 flow.

This handler does not need to be listening, and therefore it is recommended to :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler.close` the handler to avoid unnecessary listening.

Returns ``true`` if the URL matched and was handled, ``false`` otherwise.

See also `Redirect URI Schemes with Qt WebEngine <https://doc.qt.io/qt-6/qt-oauth2-browsersupport.html#redirect-uri-schemes>`_.

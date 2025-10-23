.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1da8799c415b0cb9f23a29bf07e89bb6

This slot is called by :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokens` to send the token refresh request.

The derived classes *should* reimplement this slot to support token refreshing:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.autoRefresh`, :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.accessTokenAboutToExpire`.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f68c072587c16763cbdd7f6634287d63

This function sends a token refresh request.

If the refresh request was initiated successfully, the status is set to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.RefreshingToken`; otherwise the requestFailed() signal is emitted and the status is not changed.

This function has no effect if the token refresh process is already in progress.

If refreshing the token fails and an access token exists, the status is set to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.Granted`, and to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.NotAuthenticated` if an access token does not exist.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed`, :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokens`.

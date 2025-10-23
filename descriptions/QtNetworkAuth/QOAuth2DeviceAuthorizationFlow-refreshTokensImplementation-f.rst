.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d4a60cc33f19362708fff97e7bf8e495

This function sends a token refresh request.

If the refresh request was initiated successfully, the status is set to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.RefreshingToken`; otherwise the requestFailed() signal is emitted and the status is not changed. Tokens cannot be refreshed while :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.isPolling` is ``true``.

This function has no effect if the token refresh process is already in progress.

If refreshing the token fails and an access token exists, the status is set to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.Granted`, and to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.NotAuthenticated` if an access token does not exist.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed`, :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokens`.

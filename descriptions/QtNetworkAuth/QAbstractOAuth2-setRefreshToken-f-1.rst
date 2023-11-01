.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 34b7f7e58d162e2c6242df5fc70febd3

Sets the new refresh token *refreshToken* to be used.

A custom refresh token can be used to refresh the access token via this method and then the access token can be refreshed via :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.refreshAccessToken`.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshToken`.

.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 53f0457f8eb1a6bb5f2cd4ea9289f3a7

The signal is emitted when the access token is about to expire.

Emitting this signal requires that the access token has a valid expiration time. An alternative for handling this signal manually is to use :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.autoRefresh`.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshLeadTime`, :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.autoRefresh`, :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokens`.

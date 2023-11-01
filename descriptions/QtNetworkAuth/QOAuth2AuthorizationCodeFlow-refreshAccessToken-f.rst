.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ccb4a8085f3b7d85f7e421dd5d19e9fb

Call this function to refresh the token. Access tokens are not permanent. After a time specified along with the access token when it was obtained, the access token will become invalid.

If refreshing the token fails and an access token exists, the status is set to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.Granted`, and to :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status.NotAuthenticated` otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed`, `Refresh Token <https://tools.ietf.org/html/rfc6749#section-1.5>`_.

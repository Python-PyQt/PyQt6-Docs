.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 30c287cce28083385794b71f0ea82029

Gets the current refresh token.

Refresh tokens usually have longer lifespans than access tokens, so it makes sense to save them for later use.

Returns the current refresh token or an empty string, if there is no refresh token available.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.setRefreshToken`.

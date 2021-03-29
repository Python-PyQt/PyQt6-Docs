.. sip:signal-description::
    :status: todo
    :pysig: 85f38385f6110269bb41aa0bb026967d
    :realsig: (const QNetworkProxy&,QAuthenticator*)
    :digest: a7ee2e0dc8b4d70287640d20b12e89eb

This signal can be emitted when a *proxy* that requires authentication is used. The *authenticator* object can then be filled in with the required details to allow authentication and continue the connection.

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the connection will fail if the authenticator has not been filled in with new information when the signal returns.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`.

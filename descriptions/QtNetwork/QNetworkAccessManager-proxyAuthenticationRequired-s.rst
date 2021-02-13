.. sip:signal-description::
    :status: todo
    :pysig: 85f38385f6110269bb41aa0bb026967d
    :realsig: (const QNetworkProxy&,QAuthenticator*)
    :digest: 266dce850429ddfe5342e8fca9e74252

This signal is emitted whenever a proxy requests authentication and :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` cannot find a valid, cached credential. The slot connected to this signal should fill in the credentials for the proxy *proxy* in the *authenticator* object.

:sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will cache the credentials internally. The next time the proxy requests authentication, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will automatically send the same credential without emitting the  signal again.

If the proxy rejects the credentials, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will emit the signal again.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.proxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setProxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.authenticationRequired`.

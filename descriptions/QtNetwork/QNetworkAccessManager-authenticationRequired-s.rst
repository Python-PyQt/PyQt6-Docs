.. sip:signal-description::
    :status: todo
    :pysig: aac9964fb39b835944fa9c799be7d124
    :realsig: (QNetworkReply*,QAuthenticator*)
    :digest: f879f3d5b73b36fe34e4f36376e9cffd

This signal is emitted whenever a final server requests authentication before it delivers the requested contents. The slot connected to this signal should fill the credentials for the contents (which can be determined by inspecting the *reply* object) in the *authenticator* object.

:sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will cache the credentials internally and will send the same values if the server requires authentication again, without emitting the  signal. If it rejects the credentials, this signal will be emitted again.

**Note:** To have the request not send credentials you must not call setUser() or setPassword() on the *authenticator* object. This will result in the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished` signal being emitted with a :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` with error :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.NetworkError.AuthenticationRequiredError`.

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the connection will fail if the authenticator has not been filled in with new information when the signal returns.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.proxyAuthenticationRequired`, :sip:ref:`~PyQt6.QtNetwork.QAuthenticator.setUser`, :sip:ref:`~PyQt6.QtNetwork.QAuthenticator.setPassword`.

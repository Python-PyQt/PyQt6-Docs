.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: c0f8ddb25cc0ede71b15291dbd86ca5c

Sets the password of this factory to *password*.

The password is set in the request URL when :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest` is called. The :sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` / :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will attempt to use these credentials when the server indicates that authentication is required.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.password`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.clearPassword`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.userName`.

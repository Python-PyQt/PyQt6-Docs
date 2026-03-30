.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 474d5446c9472974f5c88a4534daccb4

Sets the username of this factory to *userName*.

The username is set in the request URL when :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest` is called. The :sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` / :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will attempt to use these credentials when the server indicates that authentication is required.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.userName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.clearUserName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.password`.

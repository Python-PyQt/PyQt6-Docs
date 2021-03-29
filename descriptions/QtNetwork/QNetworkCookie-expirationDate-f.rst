.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 5ea36766fef81e8f7b9675ce4462fa9b

Returns the expiration date for this cookie. If this cookie is a session cookie, the :sip:ref:`~PyQt6.QtCore.QDateTime` returned will not be valid. If the date is in the past, this cookie has already expired and should not be sent again back to a remote server.

The expiration date corresponds to the parameters of the "expires" entry in the cookie string.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.isSessionCookie`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.setExpirationDate`.

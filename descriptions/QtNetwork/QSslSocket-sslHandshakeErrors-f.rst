.. sip:method-description::
    :status: todo
    :pysig: 84ce2c44406cfbf3b0ae9f758c0b67a4
    :realsig: () const
    :digest: 5ed17b9dd2e8181a71bd74a1d27d7d54

Returns a list of the last SSL errors that occurred. This is the same list as :sip:ref:`~PyQt6.QtNetwork.QSslSocket` passes via the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal. If the connection has been encrypted with no errors, this function will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`.

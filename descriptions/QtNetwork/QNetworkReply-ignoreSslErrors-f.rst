.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2ffc5a9bd5a9c5b0b899e2686d1b14b7

If this function is called, SSL errors related to network connection will be ignored, including certificate validation errors.

**Warning:** Be sure to always let the user inspect the errors reported by the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors` signal, and only call this method upon confirmation from the user that proceeding is ok. If there are unexpected errors, the reply should be aborted. Calling this method without inspecting the actual errors will most likely pose a security risk for your application. Use it with great care!

This function can be called from the slot connected to the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors` signal, which indicates which errors were found.

**Note:** If HTTP Strict Transport Security is enabled for :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, this function has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`.

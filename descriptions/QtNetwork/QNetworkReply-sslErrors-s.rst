.. sip:signal-description::
    :status: todo
    :pysig: 30abb1de6f61e3fb45b37bea7fd11ba3
    :realsig: (const QList<QSslError>&)
    :digest: 8ab6baedb0ab02394f55a39e94e88f9c

This signal is emitted if the SSL/TLS session encountered errors during the set up, including certificate verification errors. The *errors* parameter contains the list of errors.

To indicate that the errors are not fatal and that the connection should proceed, the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors` function should be called from the slot connected to this signal. If it is not called, the SSL session will be torn down before any data is exchanged (including the URL).

This signal can be used to display an error message to the user indicating that security may be compromised and display the SSL settings (see :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslConfiguration` to obtain it). If the user decides to proceed after analyzing the remote certificate, the slot should call :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors`.

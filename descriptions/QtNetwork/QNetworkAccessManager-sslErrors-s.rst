.. sip:signal-description::
    :status: todo
    :pysig: 873a71133403932afe68ae9795e89cfd
    :realsig: (QNetworkReply*,const QList<QSslError>&)
    :digest: ff852db42146032ee3f57bd32d1ff2a6

This signal is emitted if the SSL/TLS session encountered errors during the set up, including certificate verification errors. The *errors* parameter contains the list of errors and *reply* is the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` that is encountering these errors.

To indicate that the errors are not fatal and that the connection should proceed, the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors` function should be called from the slot connected to this signal. If it is not called, the SSL session will be torn down before any data is exchanged (including the URL).

This signal can be used to display an error message to the user indicating that security may be compromised and display the SSL settings (see sslConfiguration() to obtain it). If the user decides to proceed after analyzing the remote certificate, the slot should call ignoreSslErrors().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.ignoreSslErrors`.

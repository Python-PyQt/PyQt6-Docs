.. sip:signal-description::
    :status: todo
    :pysig: 369d07faca8949133e6e7ec0a5783a47
    :realsig: (QSslSocket*,QSsl::AlertLevel,QSsl::AlertType,const QString&)
    :digest: fe21b14a4155fb53ed9c8e035d379463

:sip:ref:`~PyQt6.QtNetwork.QSslServer` emits this signal if an alert message was sent from *socket* to a peer. *level* describes if it was a warning or a fatal error. *type* gives the code of the alert message. When a textual description of the alert message is available, it is supplied in *description*.

**Note:** This signal is mostly informational and can be used for debugging purposes, normally it does not require any actions from the application.

**Note:** Not all backends support this functionality.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.alertReceived`, QSsl::AlertLevel, QSsl::AlertType.

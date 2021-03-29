.. sip:signal-description::
    :status: todo
    :pysig: 36125a52c3439021c719cb91f2d32070
    :realsig: (QSsl::AlertLevel,QSsl::AlertType,const QString&)
    :digest: 57f47087091ff691779ae3c7f13642b7

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits this signal if an alert message was sent to a peer. *level* describes if it was a warning or a fatal error. *type* gives the code of the alert message. When a textual description of the alert message is available, it is supplied in *description*.

**Note:** This signal is mostly informational and can be used for debugging purposes, normally it does not require any actions from the application.

**Note:** Not all backends support this functionality.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.alertReceived`, QSsl::AlertLevel, QSsl::AlertType.

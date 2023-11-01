.. sip:signal-description::
    :status: todo
    :pysig: 785b10efa4cf51d8a4c8c7ca58b4af2a
    :realsig: (QSslSocket*, QSsl::AlertLevel, QSsl::AlertType, const QString&)
    :digest: 482a32e99fc0ec04af26a5e0b9bb6375

:sip:ref:`~PyQt6.QtNetwork.QSslServer` emits this signal if an alert message was received by the *socket* from a peer. *level* tells if the alert was fatal or it was a warning. *type* is the code explaining why the alert was sent. When a textual description of the alert message is available, it is supplied in *description*.

**Note:** The signal is mostly for informational and debugging purposes and does not require any handling in the application. If the alert was fatal, underlying backend will handle it and close the connection.

**Note:** Not all backends support this functionality.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.alertSent`, QSsl::AlertLevel, QSsl::AlertType.

.. sip:signal-description::
    :status: todo
    :pysig: b121962eb61015581918ff9047737dfd
    :realsig: (QSsl::AlertLevel, QSsl::AlertType, const QString&)
    :digest: dcd252813911be2b9e28061664af3121

:sip:ref:`~PyQt6.QtWebSockets.QWebSocket` emits this signal if an alert message was received from a peer. *level* tells if the alert was fatal or it was a warning. *type* is the code explaining why the alert was sent. When a textual description of the alert message is available, it is supplied in *description*.

**Note:** The signal is mostly for informational and debugging purposes and does not require any handling in the application. If the alert was fatal, underlying backend will handle it and close the connection.

**Note:** Not all backends support this functionality.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.alertSent`, QSsl::AlertLevel, QSsl::AlertType.

.. sip:signal-description::
    :status: todo
    :pysig: c4969a716a5625527e4fb7ad640404dd
    :realsig: (const QString&, QSqlDriver::NotificationSource, const QVariant&)
    :digest: b21ef387c5dc1487789aa4c1fe5ff45e

This signal is emitted when the database posts an event notification that the driver subscribes to. *name* identifies the event notification, *source* indicates the signal source, *payload* holds the extra data optionally delivered with the notification.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.subscribeToNotification`.

.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: 09ae1226dab7080fbb109af6dfde17b1

This function is called to subscribe to event notifications from the database. *name* identifies the event notification.

If successful, return true, otherwise return false.

The database must be open when this function is called. When the database is closed by calling :sip:ref:`~PyQt6.QtSql.QSqlDriver.close` all subscribed event notifications are automatically unsubscribed. Note that calling :sip:ref:`~PyQt6.QtSql.QSqlDriver.open` on an already open database may implicitly cause :sip:ref:`~PyQt6.QtSql.QSqlDriver.close` to be called, which will cause the driver to unsubscribe from all event notifications.

When an event notification identified by *name* is posted by the database the :sip:ref:`~PyQt6.QtSql.QSqlDriver.notification` signal is emitted.

Reimplement this function if you want to provide event notification support in your own :sip:ref:`~PyQt6.QtSql.QSqlDriver` subclass,

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.unsubscribeFromNotification`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.subscribedToNotifications`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`.

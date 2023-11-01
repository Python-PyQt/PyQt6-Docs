.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 536c3faef0700aeaaf09990a7473bc8e

This function is called to unsubscribe from event notifications from the database. *name* identifies the event notification.

If successful, return true, otherwise return false.

The database must be open when this function is called. All subscribed event notifications are automatically unsubscribed from when the :sip:ref:`~PyQt6.QtSql.QSqlDriver.close` function is called.

After calling *this* function the :sip:ref:`~PyQt6.QtSql.QSqlDriver.notification` signal will no longer be emitted when an event notification identified by *name* is posted by the database.

Reimplement this function if you want to provide event notification support in your own :sip:ref:`~PyQt6.QtSql.QSqlDriver` subclass,

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.subscribeToNotification`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.subscribedToNotifications`.

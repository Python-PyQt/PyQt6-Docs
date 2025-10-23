.. sip:method-description::
    :status: todo
    :pysig: d78c0dda30afdfe8349093b1cd0e5f7a
    :realsig: (const QString&, const QString&)
    :digest: 94f54f991598000bb9bd83c455dfcf96

Opens the database connection using the given *user* name and *password*. Returns ``true`` on success; otherwise returns ``false``. Error information can be retrieved using the :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` function.

This function does not store the password it is given. Instead, the password is passed directly to the driver for opening the connection and it is then discarded.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError`.

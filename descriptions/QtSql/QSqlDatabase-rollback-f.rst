.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 8e37a66ee3b028932c1b49c1fc59629e

Rolls back a transaction on the database, if the driver supports transactions and a :sip:ref:`~PyQt6.QtSql.QSqlDatabase.transaction` has been started. Returns ``true`` if the operation succeeded. Otherwise it returns ``false``.

**Note:** For some databases, the rollback will fail and return ``false`` if there is an :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` using the database for a ``SELECT``. Make the query :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` before doing the rollback.

Call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` to get information about errors.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.commit`.

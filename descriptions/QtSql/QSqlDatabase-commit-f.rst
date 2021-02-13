.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: e1174e694cdcd8e9c4ddb7d5aae086fa

Commits a transaction to the database if the driver supports transactions and a :sip:ref:`~PyQt6.QtSql.QSqlDatabase.transaction` has been started. Returns ``true`` if the operation succeeded. Otherwise it returns ``false``.

**Note:** For some databases, the commit will fail and return ``false`` if there is an :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` using the database for a ``SELECT``. Make the query :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` before doing the commit.

Call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` to get information about errors.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.rollback`.

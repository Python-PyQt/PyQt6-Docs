.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 34e22c21260c70761d2aa8f4ba5d16c8

Executes a previously prepared SQL query. Returns ``true`` if the query executed successfully; otherwise returns ``false``.

Note that the last error for this query is reset when exec() is called.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValues`.

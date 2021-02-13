.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 7a43fb879ca48444fdac00445ca070a7

Sets forward only mode to *forward*. If *forward* is true, only :sip:ref:`~PyQt6.QtSql.QSqlQuery.next` and :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek` with positive values, are allowed for navigating the results.

Forward only mode can be (depending on the driver) more memory efficient since results do not need to be cached. It will also improve performance on some databases. For this to be true, you must call ``setForwardOnly()`` before the query is prepared or executed. Note that the constructor that takes a query and a database may execute the query.

Forward only mode is off by default.

Setting forward only to false is a suggestion to the database engine, which has the final say on whether a result set is forward only or scrollable. :sip:ref:`~PyQt6.QtSql.QSqlQuery.isForwardOnly` will always return the correct status of the result set.

**Note:** Calling  after execution of the query will result in unexpected results at best, and crashes at worst.

**Note:** To make sure the forward-only query completed successfully, the application should check :sip:ref:`~PyQt6.QtSql.QSqlQuery.lastError` for an error not only after executing the query, but also after navigating the query results.

**Warning:** PostgreSQL: While navigating the query results in forward-only mode, do not execute any other SQL command on the same database connection. This will cause the query results to be lost.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isForwardOnly`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlResult.setForwardOnly`.

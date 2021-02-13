.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 1639755231e229eb096b26c106aad822

Sets forward only mode to *forward*. If *forward* is true, only :sip:ref:`~PyQt6.QtSql.QSqlResult.fetchNext` is allowed for navigating the results. Forward only mode needs much less memory since results do not have to be cached. By default, this feature is disabled.

Setting forward only to false is a suggestion to the database engine, which has the final say on whether a result set is forward only or scrollable. :sip:ref:`~PyQt6.QtSql.QSqlResult.isForwardOnly` will always return the correct status of the result set.

**Note:** Calling  after execution of the query will result in unexpected results at best, and crashes at worst.

**Note:** To make sure the forward-only query completed successfully, the application should check :sip:ref:`~PyQt6.QtSql.QSqlResult.lastError` for an error not only after executing the query, but also after navigating the query results.

**Warning:** PostgreSQL: While navigating the query results in forward-only mode, do not execute any other SQL command on the same database connection. This will cause the query results to be lost.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.isForwardOnly`, :sip:ref:`~PyQt6.QtSql.QSqlResult.fetchNext`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.setForwardOnly`.

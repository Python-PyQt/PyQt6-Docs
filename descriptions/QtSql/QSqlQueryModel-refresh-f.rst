.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5daf3ee0c1fe18fdeca1b95f74d36b9e

Re-executes the current query to fetch the data from the same database connection.

**Note:** ``refresh()`` is not applicable when the query contains bound values.

.. seealso:: setQuery(QSqlQuery &&query), :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`.

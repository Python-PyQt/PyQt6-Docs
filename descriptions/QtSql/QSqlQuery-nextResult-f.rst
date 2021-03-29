.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 2a381fbc8e28bdc34a19dde9f49454dc

Discards the current result set and navigates to the next if available.

Some databases are capable of returning multiple result sets for stored procedures or SQL batches (a query strings that contains multiple statements). If multiple result sets are available after executing a query this function can be used to navigate to the next result set(s).

If a new result set is available this function will return true. The query will be repositioned on an *invalid* record in the new result set and must be navigated to a valid record before data values can be retrieved. If a new result set isn't available the function returns ``false`` and the query is set to inactive. In any case the old result set will be discarded.

When one of the statements is a non-select statement a count of affected rows may be available instead of a result set.

Note that some databases, i.e. Microsoft SQL Server, requires non-scrollable cursors when working with multiple result sets. Some databases may execute all statements at once while others may delay the execution until the result set is actually accessed, and some databases may have restrictions on which statements are allowed to be used in a SQL batch.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.setForwardOnly`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.numRowsAffected`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.lastError`.

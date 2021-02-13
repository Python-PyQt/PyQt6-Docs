.. sip:method-description::
    :status: todo
    :pysig: 655d20e61252cd429bdaa7e9d3f8a1a0
    :realsig: (const QSqlQuery&)
    :digest: d1a9c92d8208c353bfa7a7c0f29fad47

Resets the model and sets the data provider to be the given *query*. Note that the query must be active and must not be isForwardOnly().

:sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError` can be used to retrieve verbose information if there was an error setting the query.

**Note:** Calling  will remove any inserted columns.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.query`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.setForwardOnly`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError`.

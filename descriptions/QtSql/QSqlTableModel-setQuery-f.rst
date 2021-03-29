.. sip:method-description::
    :status: todo
    :pysig: 655d20e61252cd429bdaa7e9d3f8a1a0
    :realsig: (const QSqlQuery&)
    :digest: 1c6d4142a8652ef0974346d158402d2a

This function simply calls :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.setQuery`\ (\ *query*). You should normally not call it on a :sip:ref:`~PyQt6.QtSql.QSqlTableModel`. Instead, use :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setTable`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setSort`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setFilter`, etc., to set up the query.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.selectStatement`.

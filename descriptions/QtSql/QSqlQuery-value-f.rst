.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (int) const
    :digest: 85b987ce7b3ab268fb802704ec50d590

Returns the value of field *index* in the current record.

The fields are numbered from left to right using the text of the ``SELECT`` statement, e.g. in

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqlquery_snippet.py
    :lines: 53-53

field 0 is ``forename`` and field 1 is ``surname``. Using ``SELECT \*`` is not recommended because the order of the fields in the query is undefined.

An invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is returned if field *index* does not exist, if the query is inactive, or if the query is positioned on an invalid record.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

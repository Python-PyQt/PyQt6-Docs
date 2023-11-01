.. sip:method-description::
    :status: todo
    :pysig: c2550122ef13e61aa44f09a82812494e
    :realsig: () const
    :digest: 2ad078225190d5ea98700936f1cb2149

Returns a list of bound values.

The order of the list is in binding order, irrespective of whether named or positional binding is used.

The bound values can be examined in the following way:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 208-210

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValueNames`.

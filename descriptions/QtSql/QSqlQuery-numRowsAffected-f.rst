.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 08f84886980e9c3b10bad2b41086ccfa

Returns the number of rows affected by the result's SQL statement, or -1 if it cannot be determined. Note that for ``SELECT`` statements, the value is undefined; use :sip:ref:`~PyQt6.QtSql.QSqlQuery.size` instead. If the query is not :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, -1 is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.size`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`.

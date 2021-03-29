.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d994949f4f2ac93dc22ad87df608b309

Returns the size of the result (number of rows returned), or -1 if the size cannot be determined or if the database does not support reporting information about query sizes. Note that for non-``SELECT`` statements (\ :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect` returns ``false``),  will return -1. If the query is not active (\ :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` returns ``false``), -1 is returned.

To determine the number of rows affected by a non-``SELECT`` statement, use :sip:ref:`~PyQt6.QtSql.QSqlQuery.numRowsAffected`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.numRowsAffected`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`.

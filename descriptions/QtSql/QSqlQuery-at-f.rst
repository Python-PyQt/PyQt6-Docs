.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 8a11d017cbf7307a729a34f235f0f0aa

Returns the current internal position of the query. The first record is at position zero. If the position is invalid, the function returns :sip:ref:`~PyQt6.QtSql.QSql.Location.BeforeFirstRow` or :sip:ref:`~PyQt6.QtSql.QSql.Location.AfterLastRow`, which are special negative values.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

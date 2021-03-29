.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int) const
    :digest: 4be679af67f0c1ff4693dd0cc2da5d3f

Returns ``true`` if the query is not :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, the query is not positioned on a valid record, there is no such *field*, or the *field* is null; otherwise ``false``. Note that for some drivers,  will not return accurate information until after an attempt is made to retrieve data.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.value`.

.. sip:method-description::
    :status: todo
    :pysig: 3762f7821428fbbdde024d20b06a096a
    :realsig: (int,bool)
    :digest: be5cbab8e6d4183f35f902fb85ce2697

Retrieves the record at position *index*, if available, and positions the query on the retrieved record. The first record is at position 0. Note that the query must be in an :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` state and :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect` must return true before calling this function.

If *relative* is false (the default), the following rules apply:

* If *index* is negative, the result is positioned before the first record and false is returned.

* Otherwise, an attempt is made to move to the record at position *index*. If the record at position *index* could not be retrieved, the result is positioned after the last record and false is returned. If the record is successfully retrieved, true is returned.

If *relative* is true, the following rules apply:

* If the result is currently positioned before the first record and:

  * *index* is negative or zero, there is no change, and false is returned.

  * *index* is positive, an attempt is made to position the result at absolute position *index* - 1, following the sames rule for non relative seek, above.

* If the result is currently positioned after the last record and:

  * *index* is positive or zero, there is no change, and false is returned.

  * *index* is negative, an attempt is made to position the result at *index* + 1 relative position from last record, following the rule below.

* If the result is currently located somewhere in the middle, and the relative offset *index* moves the result below zero, the result is positioned before the first record and false is returned.

* Otherwise, an attempt is made to move to the record *index* records ahead of the current record (or *index* records behind the current record if *index* is negative). If the record at offset *index* could not be retrieved, the result is positioned after the last record if *index* >= 0, (or before the first record if *index* is negative), and false is returned. If the record is successfully retrieved, true is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.at`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

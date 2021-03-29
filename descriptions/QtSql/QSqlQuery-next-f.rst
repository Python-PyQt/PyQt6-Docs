.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 25197fc84dbe3be08c9ca65daee72a8a

Retrieves the next record in the result, if available, and positions the query on the retrieved record. Note that the result must be in the :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` state and :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect` must return true before calling this function or it will do nothing and return false.

The following rules apply:

* If the result is currently located before the first record, e.g. immediately after a query is executed, an attempt is made to retrieve the first record.

* If the result is currently located after the last record, there is no change and false is returned.

* If the result is located somewhere in the middle, an attempt is made to retrieve the next record.

If the record could not be retrieved, the result is positioned after the last record and false is returned. If the record is successfully retrieved, true is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.at`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

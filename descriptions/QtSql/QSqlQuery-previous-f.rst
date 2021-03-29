.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: de9c05a9b112778007c00ec2fa9a5076

Retrieves the previous record in the result, if available, and positions the query on the retrieved record. Note that the result must be in the :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` state and :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect` must return true before calling this function or it will do nothing and return false.

The following rules apply:

* If the result is currently located before the first record, there is no change and false is returned.

* If the result is currently located after the last record, an attempt is made to retrieve the last record.

* If the result is somewhere in the middle, an attempt is made to retrieve the previous record.

If the record could not be retrieved, the result is positioned before the first record and false is returned. If the record is successfully retrieved, true is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.at`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

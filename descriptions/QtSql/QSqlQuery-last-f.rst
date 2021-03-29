.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 296b20792a965ec1fce375fef75fdbbe

Retrieves the last record in the result, if available, and positions the query on the retrieved record. Note that the result must be in the :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` state and :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect` must return true before calling this function or it will do nothing and return false. Returns ``true`` if successful. If unsuccessful the query position is set to an invalid position and false is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.at`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`.

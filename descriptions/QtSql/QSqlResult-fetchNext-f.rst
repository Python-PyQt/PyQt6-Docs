.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 910a560ef331a42d0cda2bffd4fefb42

Positions the result to the next available record (row) in the result.

This function is only called if the result is in an active state. The default implementation calls :sip:ref:`~PyQt6.QtSql.QSqlResult.fetch` with the next index. Derived classes can reimplement this function and position the result to the next record in some other way, and call :sip:ref:`~PyQt6.QtSql.QSqlResult.setAt` with an appropriate value. Return true to indicate success, or false to signify failure.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.fetch`, :sip:ref:`~PyQt6.QtSql.QSqlResult.fetchPrevious`.

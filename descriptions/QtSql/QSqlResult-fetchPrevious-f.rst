.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 3dddfafa297c20cac20cc557e61891b2

Positions the result to the previous record (row) in the result.

This function is only called if the result is in an active state. The default implementation calls :sip:ref:`~PyQt6.QtSql.QSqlResult.fetch` with the previous index. Derived classes can reimplement this function and position the result to the next record in some other way, and call :sip:ref:`~PyQt6.QtSql.QSqlResult.setAt` with an appropriate value. Return true to indicate success, or false to signify failure.

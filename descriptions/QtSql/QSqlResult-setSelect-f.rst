.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: ab063b6bc1e1997c152ec053c27224df

This function is provided for derived classes to indicate whether or not the current statement is a SQL ``SELECT`` statement. The *select* parameter should be true if the statement is a ``SELECT`` statement; otherwise it should be false.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.isSelect`.

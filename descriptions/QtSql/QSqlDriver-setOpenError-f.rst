.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 19f27358f4b990493a1812fe96403f56

This function sets the open error state of the database to *error*. Derived classes can use this function to report the status of :sip:ref:`~PyQt6.QtSql.QSqlDriver.open`. Note that if *error* is true the open state of the database is set to closed (i.e., :sip:ref:`~PyQt6.QtSql.QSqlDriver.isOpen` returns ``false``).

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.isOpenError`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.open`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.setOpen`.

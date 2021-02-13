.. sip:method-description::
    :status: todo
    :pysig: 9f473aba153c000d433dda7b7e46e713
    :realsig: () const
    :digest: 6608abdb46753bc9420c872e44d04df7

Returns the field's type as stored in the database. Note that the actual value might have a different type, Numerical values that are too large to store in a long int or double are usually stored as strings to prevent precision loss.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlField.setMetaType`, setType().

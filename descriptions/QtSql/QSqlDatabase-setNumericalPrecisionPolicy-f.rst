.. sip:method-description::
    :status: todo
    :pysig: 80192e14ee63e75c95a4edad75f33d62
    :realsig: (QSql::NumericalPrecisionPolicy)
    :digest: a8bfe34f81ae546c8c0aac86ad8b11e0

Sets the default numerical precision policy used by queries created on this database connection to *precisionPolicy*.

Note: Drivers that don't support fetching numerical values with low precision will ignore the precision policy. You can use :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature` to find out whether a driver supports this feature.

Note: Setting the default precision policy to *precisionPolicy* doesn't affect any currently active queries.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.numericalPrecisionPolicy`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.setNumericalPrecisionPolicy`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.numericalPrecisionPolicy`.

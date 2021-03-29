.. sip:method-description::
    :status: todo
    :pysig: 80192e14ee63e75c95a4edad75f33d62
    :realsig: (QSql::NumericalPrecisionPolicy)
    :digest: 7a6131a946d1e1d86c591864210d950b

Instruct the database driver to return numerical values with a precision specified by *precisionPolicy*.

The Oracle driver, for example, can retrieve numerical values as strings to prevent the loss of precision. If high precision doesn't matter, use this method to increase execution speed by bypassing string conversions.

Note: Drivers that don't support fetching numerical values with low precision will ignore the precision policy. You can use :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature` to find out whether a driver supports this feature.

Note: Setting the precision policy doesn't affect the currently active query. Call :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` or :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare` in order to activate the policy.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.numericalPrecisionPolicy`.

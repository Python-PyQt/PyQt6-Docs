.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: bed3774979f1d2c8a89e902c0f757a6c

Enables or disables the positional :ref:`qsqlquery-approaches-to-binding-values` for this query, depending on *enable* (default is ``true``). Disabling positional bindings is useful if the query itself contains a '?' which must not be handled as a positional binding parameter but, for example, as a JSON operator for a PostgreSQL database.

This function will have no effect when the database has native support for positional bindings with question marks (see also :sip:ref:`~PyQt6.QtSql.QSqlDriver.DriverFeature.PositionalPlaceholders`).

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isPositionalBindingEnabled`.

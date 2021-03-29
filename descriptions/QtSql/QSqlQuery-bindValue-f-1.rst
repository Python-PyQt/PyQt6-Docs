.. sip:method-description::
    :status: todo
    :pysig: eb2dd90d419a685b05c2d8e7af0de874
    :realsig: (int,const QVariant&,QSql::ParamType)
    :digest: a68eabdf09a45fd036f9cb73b96564a8

Set the placeholder in position *pos* to be bound to value *val* in the prepared statement. Field numbering starts at 0. If *paramType* is :sip:ref:`~PyQt6.QtSql.QSql.ParamType.Out` or :sip:ref:`~PyQt6.QtSql.QSql.ParamType.InOut`, the placeholder will be overwritten with data from the database after the :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` call.

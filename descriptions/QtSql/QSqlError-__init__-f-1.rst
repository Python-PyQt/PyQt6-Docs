.. sip:method-description::
    :status: todo
    :pysig: 3e9cc6f9c4fdc91c5743bbc0e7c66640
    :realsig: (const QString&,const QString&,QSqlError::ErrorType,const QString&)
    :digest: dec8d0c9719f7aa874ed3445082465ed

Constructs an error containing the driver error text *driverText*, the database-specific error text *databaseText*, the type *type* and the error code *code*.

**Note:** DB2: It is possible for DB2 to report more than one error code. When this happens, ``;`` is used as separator between the error codes.

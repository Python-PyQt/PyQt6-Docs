.. sip:method-description::
    :status: todo
    :pysig: 27314ba23e8180484fd826137aa04e77
    :realsig: (QSql::TableType) const
    :digest: 0523eca999a1112e75c8b6c6afaac934

Returns a list of the names of the tables in the database. The default implementation returns an empty list.

The *tableType* argument describes what types of tables should be returned. Due to binary compatibility, the string contains the value of the enum QSql::TableTypes as text. An empty string should be treated as :sip:ref:`~PyQt6.QtSql.QSql.TableType.Tables` for backward compatibility.

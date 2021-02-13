.. sip:method-description::
    :status: todo
    :pysig: 8701068106612d8405bf415e565ce2b1
    :realsig: (QSql::TableType) const
    :digest: 0523eca999a1112e75c8b6c6afaac934

Returns a list of the names of the tables in the database. The default implementation returns an empty list.

The *tableType* argument describes what types of tables should be returned. Due to binary compatibility, the string contains the value of the enum QSql::TableTypes as text. An empty string should be treated as :sip:ref:`~PyQt6.QtSql.QSql.TableType.Tables` for backward compatibility.

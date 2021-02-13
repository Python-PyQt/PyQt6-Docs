.. sip:class-description::
    :status: todo
    :brief: Encapsulates a database record
    :digest: 9043a80edddf74025e1790a25df39c15

The :sip:ref:`~PyQt6.QtSql.QSqlRecord` class encapsulates a database record.

The :sip:ref:`~PyQt6.QtSql.QSqlRecord` class encapsulates the functionality and characteristics of a database record (usually a row in a table or view within the database). :sip:ref:`~PyQt6.QtSql.QSqlRecord` supports adding and removing fields as well as setting and retrieving field values.

The values of a record's fields can be set by name or position with :sip:ref:`~PyQt6.QtSql.QSqlRecord.setValue`; if you want to set a field to null use :sip:ref:`~PyQt6.QtSql.QSqlRecord.setNull`. To find the position of a field by name use :sip:ref:`~PyQt6.QtSql.QSqlRecord.indexOf`, and to find the name of a field at a particular position use :sip:ref:`~PyQt6.QtSql.QSqlRecord.fieldName`. Use :sip:ref:`~PyQt6.QtSql.QSqlRecord.field` to retrieve a :sip:ref:`~PyQt6.QtSql.QSqlField` object for a given field. Use :sip:ref:`~PyQt6.QtSql.QSqlRecord.contains` to see if the record contains a particular field name.

When queries are generated to be executed on the database only those fields for which :sip:ref:`~PyQt6.QtSql.QSqlRecord.isGenerated` is true are included in the generated SQL.

A record can have fields added with :sip:ref:`~PyQt6.QtSql.QSqlRecord.append` or :sip:ref:`~PyQt6.QtSql.QSqlRecord.insert`, replaced with :sip:ref:`~PyQt6.QtSql.QSqlRecord.replace`, and removed with :sip:ref:`~PyQt6.QtSql.QSqlRecord.remove`. All the fields can be removed with :sip:ref:`~PyQt6.QtSql.QSqlRecord.clear`. The number of fields is given by :sip:ref:`~PyQt6.QtSql.QSqlRecord.count`; all their values can be cleared (to null) using :sip:ref:`~PyQt6.QtSql.QSqlRecord.clearValues`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlField`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.record`.

.. sip:class-description::
    :status: todo
    :brief: Manipulates the fields in SQL database tables and views
    :digest: 00b2ee545b038fc4285cb79ba507d0fd

The :sip:ref:`~PyQt6.QtSql.QSqlField` class manipulates the fields in SQL database tables and views.

:sip:ref:`~PyQt6.QtSql.QSqlField` represents the characteristics of a single column in a database table or view, such as the data type and column name. A field also contains the value of the database column, which can be viewed or changed.

Field data values are stored as QVariants. Using an incompatible type is not permitted. For example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 85-86

However, the field will attempt to cast certain data types to the field data type where possible:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 93-94

:sip:ref:`~PyQt6.QtSql.QSqlField` objects are rarely created explicitly in application code. They are usually accessed indirectly through :sip:ref:`~PyQt6.QtSql.QSqlRecord`\ s that already contain a list of fields. For example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 100-100

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 102-102

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 104-104

A :sip:ref:`~PyQt6.QtSql.QSqlField` object can provide some meta-data about the field, for example, its :sip:ref:`~PyQt6.QtSql.QSqlField.name`, variant , :sip:ref:`~PyQt6.QtSql.QSqlField.length`, :sip:ref:`~PyQt6.QtSql.QSqlField.precision`, :sip:ref:`~PyQt6.QtSql.QSqlField.defaultValue`, , and its :sip:ref:`~PyQt6.QtSql.QSqlField.requiredStatus`, :sip:ref:`~PyQt6.QtSql.QSqlField.isGenerated` and :sip:ref:`~PyQt6.QtSql.QSqlField.isReadOnly`. The field's data can be checked to see if it :sip:ref:`~PyQt6.QtSql.QSqlField.isNull`, and its :sip:ref:`~PyQt6.QtSql.QSqlField.value` retrieved. When editing the data can be set with :sip:ref:`~PyQt6.QtSql.QSqlField.setValue` or set to NULL with :sip:ref:`~PyQt6.QtSql.QSqlField.clear`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord`.

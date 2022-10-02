.. sip:method-description::
    :status: todo
    :pysig: 10e872425c19a889993f2239558a341c
    :realsig: (QSqlQuery::BatchExecutionMode)
    :digest: 2286c32dd16651d49fc241cf4b72e368

Executes a previously prepared SQL query in a batch. All the bound parameters have to be lists of variants. If the database doesn't support batch executions, the driver will simulate it using conventional :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` calls.

Returns ``true`` if the query is executed successfully; otherwise returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqlquery.py
    :lines: 70-82

The example above inserts four new rows into ``myTable``:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqlquery_snippet.py
    :lines: 56-59

To bind NULL values, a null :sip:ref:`~PyQt6.QtCore.QVariant` of the relevant type has to be added to the bound QVariantList; for example, ``QVariant(QMetaType::fromType<QString>())`` should be used if you are using strings.

**Note:** Every bound QVariantList must contain the same amount of variants.

**Note:** The type of the QVariants in a list must not change. For example, you cannot mix integer and string variants within a QVariantList.

The *mode* parameter indicates how the bound QVariantList will be interpreted. If *mode* is ``ValuesAsRows``, every variant within the QVariantList will be interpreted as a value for a new row. ``ValuesAsColumns`` is a special case for the Oracle driver. In this mode, every entry within a QVariantList will be interpreted as array-value for an IN or OUT value within a stored procedure. Note that this will only work if the IN or OUT value is a table-type consisting of only one column of a basic type, for example ``TYPE myType IS TABLE OF VARCHAR(64) INDEX BY BINARY_INTEGER;``

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`.

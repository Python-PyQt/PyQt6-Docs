.. sip:method-description::
    :status: todo
    :pysig: 8f18be08ed9d3ffb308d766f0f9273db
    :realsig: (QSqlDriver::StatementType, const QString&, const QSqlRecord&, bool) const
    :digest: 47d74e9c94214dc2a7c147efe26eaf04

Returns a SQL statement of type *type* for the table *tableName* with the values from *rec*. If *preparedStatement* is true, the string will contain placeholders instead of values.

The generated flag in each field of *rec* determines whether the field is included in the generated statement.

This method can be used to manipulate tables without having to worry about database-dependent SQL dialects. For non-prepared statements, the values will be properly escaped.

In the WHERE statement, each non-null field of *rec* specifies a filter condition of equality to the field value, or if prepared, a placeholder. However, prepared or not, a null field specifies the condition IS NULL and never introduces a placeholder. The application must not attempt to bind data for the null field during execution. The field must be set to some non-null value if a placeholder is desired. Furthermore, since non-null fields specify equality conditions and SQL NULL is not equal to anything, even itself, it is generally not useful to bind a null to a placeholder.

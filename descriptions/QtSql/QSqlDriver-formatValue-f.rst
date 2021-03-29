.. sip:method-description::
    :status: todo
    :pysig: 0cdedcd80125dc9f43245807d5f95fe3
    :realsig: (const QSqlField&,bool) const
    :digest: 645375bb6fe4961cfeb1559255bc15ab

Returns a string representation of the *field* value for the database. This is used, for example, when constructing INSERT and UPDATE statements.

The default implementation returns the value formatted as a string according to the following rules:

* If *field* is character data, the value is returned enclosed in single quotation marks, which is appropriate for many SQL databases. Any embedded single-quote characters are escaped (replaced with two single-quote characters). If *trimStrings* is true (the default is false), all trailing whitespace is trimmed from the field.

* If *field* is date/time data, the value is formatted in ISO format and enclosed in single quotation marks. If the date/time data is invalid, "NULL" is returned.

* If *field* is :sip:ref:`~PyQt6.QtCore.QByteArray` data, and the driver can edit binary fields, the value is formatted as a hexadecimal string.

* For any other field type, toString() is called on its value and the result of this is returned.

.. seealso:: QVariant::toString().

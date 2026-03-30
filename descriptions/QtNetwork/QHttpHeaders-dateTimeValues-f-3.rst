.. sip:method-description::
    :status: todo
    :pysig: f8de93ca5c17df2d47cafb8002a14a2d
    :realsig: (QAnyStringView) const
    :digest: 9539bf2df34892eab0033c712f414e42

Returns all the header values of *name* in a list of :sip:ref:`~PyQt6.QtCore.QDateTime` objects, following the standard HTTP date formats. If no valid date-time values are found, returns ``std::nullopt``.

.. seealso:: dateTimeValue(QAnyStringView name), dateTimeValueAt(qsizetype i).

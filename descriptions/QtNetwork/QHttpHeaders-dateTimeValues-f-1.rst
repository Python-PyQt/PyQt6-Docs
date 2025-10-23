.. sip:method-description::
    :status: todo
    :pysig: 4460896efa546cff0cd1abc346c67bfc
    :realsig: (QAnyStringView) const
    :digest: 9539bf2df34892eab0033c712f414e42

Returns all the header values of *name* in a list of :sip:ref:`~PyQt6.QtCore.QDateTime` objects, following the standard HTTP date formats. If no valid date-time values are found, returns ``std::nullopt``.

.. seealso:: dateTimeValue(QAnyStringView name), dateTimeValueAt(qsizetype i).

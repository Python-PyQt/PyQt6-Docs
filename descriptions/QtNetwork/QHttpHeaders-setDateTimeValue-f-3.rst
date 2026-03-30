.. sip:method-description::
    :status: todo
    :pysig: 3f4dd9cdb62fa3ae8adb5d5ac7420e0c
    :realsig: (QAnyStringView, const QDateTime&)
    :digest: 88eb617da0a301eeda8f63c102591970

Sets the value of the header name *name* to *dateTime*, following the `standard HTTP IMF-fixdate format <https://datatracker.ietf.org/doc/html/rfc9110#name-date-time-formats>`_. If the header does not exist, adds a new one.

.. seealso:: dateTimeValue(QAnyStringView name), dateTimeValueAt(qsizetype i).

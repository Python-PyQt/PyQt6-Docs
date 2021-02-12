.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: b1b8d26e203e432b6b5c91b8d1c25141

Returns the number of seconds from this datetime to the *other* datetime. If the *other* datetime is earlier than this datetime, the value returned is negative.

Before performing the comparison, the two datetimes are converted to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` to ensure that the result is correct if daylight-saving (DST) applies to one of the two datetimes but not the other.

Returns 0 if either datetime is invalid.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 132-134

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`, :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo`, :sip:ref:`~PyQt6.QtCore.QTime.secsTo`.

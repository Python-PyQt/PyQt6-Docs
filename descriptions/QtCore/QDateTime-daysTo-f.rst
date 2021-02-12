.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: 8e9eae75727ae690d09fee7d73f1d6c1

Returns the number of days from this datetime to the *other* datetime. The number of days is counted as the number of times midnight is reached between this datetime to the *other* datetime. This means that a 10 minute difference from 23:55 to 0:05 the next day counts as one day.

If the *other* datetime is earlier than this datetime, the value returned is negative.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 163-172

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.addDays`, :sip:ref:`~PyQt6.QtCore.QDateTime.secsTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.msecsTo`.

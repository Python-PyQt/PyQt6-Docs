.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 83eb023eea4f0ea5f2a64447a0b5a9f7

Returns a copy of this datetime converted to the given *timeZone*.

The result represents the same moment in time as, and is equal to, this datetime.

The result describes the moment in time in terms of *timeZone*'s time representation. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py

If *timeZone* is invalid then the datetime will be invalid. Otherwise the returned datetime's :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will match ``timeZone.timeSpec()``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation`, :sip:ref:`~PyQt6.QtCore.QDateTime.toLocalTime`, :sip:ref:`~PyQt6.QtCore.QDateTime.toUTC`, :sip:ref:`~PyQt6.QtCore.QDateTime.toOffsetFromUtc`.

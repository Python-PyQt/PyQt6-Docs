.. sip:method-description::
    :status: todo
    :pysig: 41145246d08568577980f08c1fee338e
    :realsig: (Qt::TimeSpec)
    :digest: 5c6c2d41cd58655e3c4bf0b909a1658f

Use :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone` instead

Sets the time specification used in this datetime to *spec*. The datetime may refer to a different point in time.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, i.e. an effective offset of 0.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the spec will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the current system time zone.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 200-207

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.setDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTime`.

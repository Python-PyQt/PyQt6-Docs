.. sip:method-description::
    :status: todo
    :pysig: 04b1f98fda76754e0834d43b3c521300
    :realsig: (Qt::TimeSpec) const
    :digest: dcc284752d8372966cf00a296d3c75e4

Use :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone` instead.

Returns a copy of this datetime converted to the given time *spec*.

The result represents the same moment in time as, and is equal to, this datetime.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then it is set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`. To set to a fixed offset from UTC, use :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone` or :sip:ref:`~PyQt6.QtCore.QDateTime.toOffsetFromUtc`.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then it is set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the local Time Zone. To set a specified time-zone, use :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 176-180

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone`.

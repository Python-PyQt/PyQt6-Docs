.. sip:method-description::
    :status: todo
    :pysig: 04b1f98fda76754e0834d43b3c521300
    :realsig: (Qt::TimeSpec) const
    :digest: 6fa6cf2266ea4a19da95ef2013e802fc

Returns a copy of this datetime converted to the given time *spec*.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then it is set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`. To set to a spec of :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` use :sip:ref:`~PyQt6.QtCore.QDateTime.toOffsetFromUtc`.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then it is set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the local Time Zone.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 176-180

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime.toOffsetFromUtc`.

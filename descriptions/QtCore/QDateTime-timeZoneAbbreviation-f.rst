.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a7f68a6f941530a1d7d2529d1305c6b7

Returns the Time Zone Abbreviation for this datetime.

The returned string depends on :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`:

* For :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` it is "UTC".

* For :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` it will be in the format "UTC[+-]00:00".

* For :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, the host system is queried.

* For :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`, the associated :sip:ref:`~PyQt6.QtCore.QTimeZone` object is queried.

**Note:** The abbreviation is not guaranteed to be unique, i.e. different time zones may have the same abbreviation. For :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` and :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`, when returned by the host system, the abbreviation may be localized.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`, :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

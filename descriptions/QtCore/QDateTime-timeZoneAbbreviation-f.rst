.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 19c9fb307f60666cefa509f27806c229

Returns the Time Zone Abbreviation for the datetime.

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` this will be "UTC".

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` this will be in the format "UTC[+-]00:00".

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` then the host system is queried for the correct abbreviation.

Note that abbreviations may or may not be localized.

Note too that the abbreviation is not guaranteed to be a unique value, i.e. different time zones may have the same abbreviation.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`.

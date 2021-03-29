.. sip:method-description::
    :status: todo
    :pysig: 8e2eb029a1edf7b5c64e6b25f7203431
    :realsig: (QDate,QTime,Qt::TimeSpec,int)
    :digest: 6f816ed1e14907862eb6e43881b5226f

Constructs a datetime with the given *date* and *time*, using the time specification defined by *spec* and *offsetSeconds* seconds.

If *date* is valid and *time* is not, the time will be set to midnight.

If the *spec* is not :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then *offsetSeconds* will be ignored.

If the *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` and *offsetSeconds* is 0 then the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, i.e. an offset of 0 seconds.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the spec will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the current system time zone. To create a :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` datetime use the correct constructor.

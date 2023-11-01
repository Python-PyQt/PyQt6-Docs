:orphan:

.. sip:class:: PyQt6.QtCore.QDateTime
    :description: QtCore/QDateTime-c.rst

    .. sip:enum:: PyQt6.QtCore.QDateTime.YearRange
        :description: QtCore/QDateTime-YearRange-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDateTime.YearRange.First
            :description: QtCore/QDateTime-YearRange-First-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDateTime.YearRange.Last
            :description: QtCore/QDateTime-YearRange-Last-v.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__init__
        :description: QtCore/QDateTime-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :description: QtCore/QDateTime-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
            Union[:sip:ref:`~PyQt6.QtCore.QTime`, datetime.time]
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QDateTime-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
            Union[:sip:ref:`~PyQt6.QtCore.QTime`, datetime.time]
            spec: :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` = :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`
            offsetSeconds: int = 0
        :description: QtCore/QDateTime-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__init__
        :args:
            int
            int
            int
            int
            int
            second: int = 0
            msec: int = 0
            timeSpec: int = 0
        :description: QtCore/QDateTime-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.addDays
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-addDays-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.addMonths
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-addMonths-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.addMSecs
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-addMSecs-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.addSecs
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-addSecs-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.addYears
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-addYears-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__bool__
        :returns:
            int
        :description: QtCore/QDateTime-__bool__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.currentDateTime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-currentDateTime-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.currentDateTime
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-currentDateTime-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.currentDateTimeUtc
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-currentDateTimeUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.currentMSecsSinceEpoch
        :returns:
            int
        :static:
        :description: QtCore/QDateTime-currentMSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.currentSecsSinceEpoch
        :returns:
            int
        :static:
        :description: QtCore/QDateTime-currentSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.date
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDateTime-date-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.daysTo
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QDateTime-daysTo-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__eq__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromMSecsSinceEpoch
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromMSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromMSecsSinceEpoch
        :args:
            int
            spec: :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` = :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`
            offsetSeconds: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromMSecsSinceEpoch-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromSecsSinceEpoch
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromSecsSinceEpoch
        :args:
            int
            spec: :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` = :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`
            offsetSeconds: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromSecsSinceEpoch-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromString
        :args:
            Optional[str]
            format: :sip:ref:`~PyQt6.QtCore.Qt.DateFormat` = :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromString-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.fromString
        :args:
            Optional[str]
            Optional[str]
            cal: :sip:ref:`~PyQt6.QtCore.QCalendar` = QCalendar()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :static:
        :description: QtCore/QDateTime-fromString-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__ge__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__ge__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__gt__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__gt__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__hash__
        :returns:
            int
        :description: QtCore/QDateTime-__hash__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.isDaylightTime
        :returns:
            bool
        :description: QtCore/QDateTime-isDaylightTime-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.isNull
        :returns:
            bool
        :description: QtCore/QDateTime-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.isValid
        :returns:
            bool
        :description: QtCore/QDateTime-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__le__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__le__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__lt__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__lt__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.msecsTo
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QDateTime-msecsTo-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__ne__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QDateTime-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.offsetFromUtc
        :returns:
            int
        :description: QtCore/QDateTime-offsetFromUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.__repr__
        :returns:
            str
        :description: QtCore/QDateTime-__repr__-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.secsTo
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QDateTime-secsTo-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtCore/QDateTime-setDate-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setMSecsSinceEpoch
        :args:
            int
        :description: QtCore/QDateTime-setMSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setOffsetFromUtc
        :args:
            int
        :description: QtCore/QDateTime-setOffsetFromUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setSecsSinceEpoch
        :args:
            int
        :description: QtCore/QDateTime-setSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setTime
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QTime`, datetime.time]
        :description: QtCore/QDateTime-setTime-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setTimeSpec
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`
        :description: QtCore/QDateTime-setTimeSpec-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.setTimeZone
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QDateTime-setTimeZone-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.time
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTime`
        :description: QtCore/QDateTime-time-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.timeRepresentation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QDateTime-timeRepresentation-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.timeSpec
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`
        :description: QtCore/QDateTime-timeSpec-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.timeZone
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QDateTime-timeZone-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.timeZoneAbbreviation
        :returns:
            str
        :description: QtCore/QDateTime-timeZoneAbbreviation-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toLocalTime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-toLocalTime-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toMSecsSinceEpoch
        :returns:
            int
        :description: QtCore/QDateTime-toMSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toOffsetFromUtc
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-toOffsetFromUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toPyDateTime
        :returns:
            datetime.datetime
        :description: QtCore/QDateTime-toPyDateTime-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toSecsSinceEpoch
        :returns:
            int
        :description: QtCore/QDateTime-toSecsSinceEpoch-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toString
        :args:
            format: :sip:ref:`~PyQt6.QtCore.Qt.DateFormat` = :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`
        :returns:
            str
        :description: QtCore/QDateTime-toString-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toString
        :args:
            Optional[str]
            cal: :sip:ref:`~PyQt6.QtCore.QCalendar` = QCalendar()
        :returns:
            str
        :description: QtCore/QDateTime-toString-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toTimeSpec
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-toTimeSpec-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toTimeZone
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-toTimeZone-f.rst

    .. sip:method:: PyQt6.QtCore.QDateTime.toUTC
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDateTime-toUTC-f.rst

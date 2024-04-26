:orphan:

.. sip:class:: PyQt6.QtCore.QDate
    :description: QtCore/QDate-c.rst

    .. sip:method:: PyQt6.QtCore.QDate.__init__
        :description: QtCore/QDate-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.__init__
        :args:
            int
            int
            int
        :description: QtCore/QDate-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDate.__init__
        :args:
            int
            int
            int
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :description: QtCore/QDate-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDate.addDays
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-addDays-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.addMonths
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-addMonths-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.addMonths
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-addMonths-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.addYears
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-addYears-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.addYears
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QDate-addYears-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.__bool__
        :returns:
            int
        :description: QtCore/QDate-__bool__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.currentDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :static:
        :description: QtCore/QDate-currentDate-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.day
        :returns:
            int
        :description: QtCore/QDate-day-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.day
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-day-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.dayOfWeek
        :returns:
            int
        :description: QtCore/QDate-dayOfWeek-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.dayOfWeek
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-dayOfWeek-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.dayOfYear
        :returns:
            int
        :description: QtCore/QDate-dayOfYear-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.dayOfYear
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-dayOfYear-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.daysInMonth
        :returns:
            int
        :description: QtCore/QDate-daysInMonth-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.daysInMonth
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-daysInMonth-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.daysInYear
        :returns:
            int
        :description: QtCore/QDate-daysInYear-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.daysInYear
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-daysInYear-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.daysTo
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            int
        :description: QtCore/QDate-daysTo-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.endOfDay
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDate-endOfDay-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.endOfDay
        :args:
            spec: :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` = :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`
            offsetSeconds: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDate-endOfDay-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.__eq__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.fromJulianDay
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :static:
        :description: QtCore/QDate-fromJulianDay-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.fromString
        :args:
            Optional[str]
            format: :sip:ref:`~PyQt6.QtCore.Qt.DateFormat` = :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :static:
        :description: QtCore/QDate-fromString-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDate.fromString
        :args:
            Optional[str]
            Optional[str]
            cal: :sip:ref:`~PyQt6.QtCore.QCalendar` = QCalendar()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :static:
        :description: QtCore/QDate-fromString-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDate.fromString
        :args:
            Optional[str]
            Optional[str]
            int
            cal: :sip:ref:`~PyQt6.QtCore.QCalendar` = QCalendar()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :static:
        :description: QtCore/QDate-fromString-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDate.__ge__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__ge__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.getDate
        :returns:
            int
            int
            int
        :description: QtCore/QDate-getDate-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.__gt__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__gt__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.__hash__
        :returns:
            int
        :description: QtCore/QDate-__hash__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.isLeapYear
        :args:
            int
        :returns:
            bool
        :static:
        :description: QtCore/QDate-isLeapYear-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.isNull
        :returns:
            bool
        :description: QtCore/QDate-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.isValid
        :returns:
            bool
        :description: QtCore/QDate-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.isValid
        :args:
            int
            int
            int
        :returns:
            bool
        :static:
        :description: QtCore/QDate-isValid-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.__le__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__le__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.__lt__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__lt__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.month
        :returns:
            int
        :description: QtCore/QDate-month-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.month
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-month-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.__ne__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            bool
        :description: QtCore/QDate-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.__repr__
        :returns:
            str
        :description: QtCore/QDate-__repr__-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.setDate
        :args:
            int
            int
            int
        :returns:
            bool
        :description: QtCore/QDate-setDate-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.setDate
        :args:
            int
            int
            int
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            bool
        :description: QtCore/QDate-setDate-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.startOfDay
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDate-startOfDay-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.startOfDay
        :args:
            spec: :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` = :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`
            offsetSeconds: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QDate-startOfDay-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDate.toJulianDay
        :returns:
            int
        :description: QtCore/QDate-toJulianDay-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.toPyDate
        :returns:
            datetime.date
        :description: QtCore/QDate-toPyDate-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.toString
        :args:
            format: :sip:ref:`~PyQt6.QtCore.Qt.DateFormat` = :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`
        :returns:
            str
        :description: QtCore/QDate-toString-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.toString
        :args:
            Optional[str]
            cal: :sip:ref:`~PyQt6.QtCore.QCalendar` = QCalendar()
        :returns:
            str
        :description: QtCore/QDate-toString-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDate.weekNumber
        :returns:
            int
            int
        :description: QtCore/QDate-weekNumber-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.year
        :returns:
            int
        :description: QtCore/QDate-year-f.rst

    .. sip:method:: PyQt6.QtCore.QDate.year
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :returns:
            int
        :description: QtCore/QDate-year-f-1.rst

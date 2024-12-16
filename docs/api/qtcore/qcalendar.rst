:orphan:

.. sip:class:: PyQt6.QtCore.QCalendar
    :description: QtCore/QCalendar-c.rst

    .. sip:enum:: PyQt6.QtCore.QCalendar.System
        :description: QtCore/QCalendar-System-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCalendar.System.Gregorian
            :description: QtCore/QCalendar-System-Gregorian-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCalendar.System.IslamicCivil
            :description: QtCore/QCalendar-System-IslamicCivil-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCalendar.System.Jalali
            :description: QtCore/QCalendar-System-Jalali-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCalendar.System.Julian
            :description: QtCore/QCalendar-System-Julian-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCalendar.System.Milankovic
            :description: QtCore/QCalendar-System-Milankovic-v.rst

    .. sip:attribute:: PyQt6.QtCore.QCalendar.Unspecified
        :type: int
        :const:
        :description: QtCore/QCalendar-Unspecified-a.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.__init__
        :description: QtCore/QCalendar-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar.System`
        :description: QtCore/QCalendar-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.__init__
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtCore/QCalendar-__init__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :description: QtCore/QCalendar-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.availableCalendars
        :returns:
            list[str]
        :static:
        :description: QtCore/QCalendar-availableCalendars-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.dateFromParts
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar.YearMonthDay`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QCalendar-dateFromParts-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.dateFromParts
        :args:
            int
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QCalendar-dateFromParts-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.dateTimeToString
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
            Union[:sip:ref:`~PyQt6.QtCore.QTime`, datetime.time]
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :returns:
            str
        :description: QtCore/QCalendar-dateTimeToString-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.dayOfWeek
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            int
        :description: QtCore/QCalendar-dayOfWeek-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.daysInMonth
        :args:
            int
            year: int = :sip:ref:`~PyQt6.QtCore.QCalendar.Unspecified`
        :returns:
            int
        :description: QtCore/QCalendar-daysInMonth-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.daysInYear
        :args:
            int
        :returns:
            int
        :description: QtCore/QCalendar-daysInYear-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.hasYearZero
        :returns:
            bool
        :description: QtCore/QCalendar-hasYearZero-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isDateValid
        :args:
            int
            int
            int
        :returns:
            bool
        :description: QtCore/QCalendar-isDateValid-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isGregorian
        :returns:
            bool
        :description: QtCore/QCalendar-isGregorian-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isLeapYear
        :args:
            int
        :returns:
            bool
        :description: QtCore/QCalendar-isLeapYear-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isLunar
        :returns:
            bool
        :description: QtCore/QCalendar-isLunar-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isLuniSolar
        :returns:
            bool
        :description: QtCore/QCalendar-isLuniSolar-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isProleptic
        :returns:
            bool
        :description: QtCore/QCalendar-isProleptic-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.isSolar
        :returns:
            bool
        :description: QtCore/QCalendar-isSolar-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.matchCenturyToWeekday
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar.YearMonthDay`
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtCore/QCalendar-matchCenturyToWeekday-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.maximumDaysInMonth
        :returns:
            int
        :description: QtCore/QCalendar-maximumDaysInMonth-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.maximumMonthsInYear
        :returns:
            int
        :description: QtCore/QCalendar-maximumMonthsInYear-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.minimumDaysInMonth
        :returns:
            int
        :description: QtCore/QCalendar-minimumDaysInMonth-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.monthName
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            int
            year: int = :sip:ref:`~PyQt6.QtCore.QCalendar.Unspecified`
            format: :sip:ref:`~PyQt6.QtCore.QLocale.FormatType` = :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`
        :returns:
            str
        :description: QtCore/QCalendar-monthName-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.monthsInYear
        :args:
            int
        :returns:
            int
        :description: QtCore/QCalendar-monthsInYear-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.name
        :returns:
            str
        :description: QtCore/QCalendar-name-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.partsFromDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCalendar.YearMonthDay`
        :description: QtCore/QCalendar-partsFromDate-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.standaloneMonthName
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            int
            year: int = :sip:ref:`~PyQt6.QtCore.QCalendar.Unspecified`
            format: :sip:ref:`~PyQt6.QtCore.QLocale.FormatType` = :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`
        :returns:
            str
        :description: QtCore/QCalendar-standaloneMonthName-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.standaloneWeekDayName
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            int
            format: :sip:ref:`~PyQt6.QtCore.QLocale.FormatType` = :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`
        :returns:
            str
        :description: QtCore/QCalendar-standaloneWeekDayName-f.rst

    .. sip:method:: PyQt6.QtCore.QCalendar.weekDayName
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            int
            format: :sip:ref:`~PyQt6.QtCore.QLocale.FormatType` = :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`
        :returns:
            str
        :description: QtCore/QCalendar-weekDayName-f.rst

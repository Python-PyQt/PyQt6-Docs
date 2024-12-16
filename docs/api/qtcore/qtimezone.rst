:orphan:

.. sip:class:: PyQt6.QtCore.QTimeZone
    :description: QtCore/QTimeZone-c.rst

    .. sip:enum:: PyQt6.QtCore.QTimeZone.Initialization
        :description: QtCore/QTimeZone-Initialization-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.Initialization.LocalTime
            :description: QtCore/QTimeZone-Initialization-LocalTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.Initialization.UTC
            :description: QtCore/QTimeZone-Initialization-UTC-v.rst

    .. sip:enum:: PyQt6.QtCore.QTimeZone.NameType
        :description: QtCore/QTimeZone-NameType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.NameType.DefaultName
            :description: QtCore/QTimeZone-NameType-DefaultName-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.NameType.LongName
            :description: QtCore/QTimeZone-NameType-LongName-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.NameType.OffsetName
            :description: QtCore/QTimeZone-NameType-OffsetName-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.NameType.ShortName
            :description: QtCore/QTimeZone-NameType-ShortName-v.rst

    .. sip:enum:: PyQt6.QtCore.QTimeZone.TimeType
        :description: QtCore/QTimeZone-TimeType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.TimeType.DaylightTime
            :description: QtCore/QTimeZone-TimeType-DaylightTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.TimeType.GenericTime
            :description: QtCore/QTimeZone-TimeType-GenericTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTimeZone.TimeType.StandardTime
            :description: QtCore/QTimeZone-TimeType-StandardTime-v.rst

    .. sip:attribute:: PyQt6.QtCore.QTimeZone.MaxUtcOffsetSecs
        :type: int
        :const:
        :static:
        :description: QtCore/QTimeZone-MaxUtcOffsetSecs-a.rst

    .. sip:attribute:: PyQt6.QtCore.QTimeZone.MinUtcOffsetSecs
        :type: int
        :const:
        :static:
        :description: QtCore/QTimeZone-MinUtcOffsetSecs-a.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :description: QtCore/QTimeZone-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization`
        :description: QtCore/QTimeZone-__init__-f-6.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QTimeZone-__init__-f-7.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            int
        :description: QtCore/QTimeZone-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QTimeZone-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            int
            Optional[str]
            Optional[str]
            territory: :sip:ref:`~PyQt6.QtCore.QLocale.Country` = :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory`
            comment: Optional[str] = ''
        :description: QtCore/QTimeZone-__init__-f-8.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.abbreviation
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            str
        :description: QtCore/QTimeZone-abbreviation-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.asBackendZone
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QTimeZone-asBackendZone-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f-4.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :args:
            int
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f-5.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.comment
        :returns:
            str
        :description: QtCore/QTimeZone-comment-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.country
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :description: QtCore/QTimeZone-country-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.daylightTimeOffset
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QTimeZone-daylightTimeOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.displayName
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
            nameType: :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType` = :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.DefaultName`
            locale: :sip:ref:`~PyQt6.QtCore.QLocale` = QLocale()
        :returns:
            str
        :description: QtCore/QTimeZone-displayName-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.displayName
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone.TimeType`
            nameType: :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType` = :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.DefaultName`
            locale: :sip:ref:`~PyQt6.QtCore.QLocale` = QLocale()
        :returns:
            str
        :description: QtCore/QTimeZone-displayName-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            bool
        :description: QtCore/QTimeZone-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.fixedSecondsAheadOfUtc
        :returns:
            int
        :description: QtCore/QTimeZone-fixedSecondsAheadOfUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.fromSecondsAheadOfUtc
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :static:
        :description: QtCore/QTimeZone-fromSecondsAheadOfUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.hasAlternativeName
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtCore/QTimeZone-hasAlternativeName-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.hasDaylightTime
        :returns:
            bool
        :description: QtCore/QTimeZone-hasDaylightTime-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.hasTransitions
        :returns:
            bool
        :description: QtCore/QTimeZone-hasTransitions-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.ianaIdToWindowsId
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-ianaIdToWindowsId-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.id
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QTimeZone-id-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.isDaylightTime
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            bool
        :description: QtCore/QTimeZone-isDaylightTime-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :static:
        :description: QtCore/QTimeZone-isTimeZoneIdAvailable-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.isUtcOrFixedOffset
        :returns:
            bool
        :description: QtCore/QTimeZone-isUtcOrFixedOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.isUtcOrFixedOffset
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`
        :returns:
            bool
        :static:
        :description: QtCore/QTimeZone-isUtcOrFixedOffset-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.isValid
        :returns:
            bool
        :description: QtCore/QTimeZone-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            bool
        :description: QtCore/QTimeZone-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.nextTransition
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData`
        :description: QtCore/QTimeZone-nextTransition-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.offsetData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData`
        :description: QtCore/QTimeZone-offsetData-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.offsetFromUtc
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QTimeZone-offsetFromUtc-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.previousTransition
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData`
        :description: QtCore/QTimeZone-previousTransition-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.standardTimeOffset
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            int
        :description: QtCore/QTimeZone-standardTimeOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :description: QtCore/QTimeZone-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.systemTimeZone
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :static:
        :description: QtCore/QTimeZone-systemTimeZone-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.systemTimeZoneId
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-systemTimeZoneId-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.territory
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :description: QtCore/QTimeZone-territory-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.timeSpec
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`
        :description: QtCore/QTimeZone-timeSpec-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.transitions
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData`]
        :description: QtCore/QTimeZone-transitions-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.utc
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :static:
        :description: QtCore/QTimeZone-utc-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-windowsIdToDefaultIanaId-f-2.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-windowsIdToDefaultIanaId-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToIanaIds
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-windowsIdToIanaIds-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToIanaIds
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-windowsIdToIanaIds-f-1.rst

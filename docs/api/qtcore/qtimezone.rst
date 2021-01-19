:orphan:

.. sip:class:: PyQt6.QtCore.QTimeZone
    :description: QtCore/QTimeZone-c.rst

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

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :description: QtCore/QTimeZone-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QTimeZone-__init__-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            int
            str
            str
            country: :sip:ref:`~PyQt6.QtCore.QLocale.Country` = :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry`
            comment: str = ''
        :description: QtCore/QTimeZone-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.abbreviation
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            str
        :description: QtCore/QTimeZone-abbreviation-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.availableTimeZoneIds
        :args:
            int
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-availableTimeZoneIds-f-2.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-ianaIdToWindowsId-f.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :static:
        :description: QtCore/QTimeZone-isTimeZoneIdAvailable-f.rst

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

    .. sip:method:: PyQt6.QtCore.QTimeZone.transitions
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData`]
        :description: QtCore/QTimeZone-transitions-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.utc
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :static:
        :description: QtCore/QTimeZone-utc-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-windowsIdToDefaultIanaId-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QTimeZone-windowsIdToDefaultIanaId-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToIanaIds
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-windowsIdToIanaIds-f.rst

    .. sip:method:: PyQt6.QtCore.QTimeZone.windowsIdToIanaIds
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtCore.QLocale.Country`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtCore/QTimeZone-windowsIdToIanaIds-f-1.rst

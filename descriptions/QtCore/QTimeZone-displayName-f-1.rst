.. sip:method-description::
    :status: todo
    :pysig: fa76660ed289d70dbd7dba1b5c85cbef
    :realsig: (QTimeZone::TimeType,QTimeZone::NameType,const QLocale&) const
    :digest: f53e85fcf79d6019be1b8da8d0738d65

Returns the localized time zone display name.

The name returned is the one for the given *locale*, applicable when the given *timeType* is in effect and of the form indicated by *nameType*. Where the time zone display names have changed over time, the current names will be used. If no suitably localized name of the given type is available, another name type may be used, or an empty string may be returned.

If the *locale* is not provided, then the application default locale will be used. For custom timezones created by client code, the data supplied to the constructor are used, as no localization data will be available for it. If this timezone is invalid, an empty string is returned. This may also arise for the representation of local time if determining the system time zone fails.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

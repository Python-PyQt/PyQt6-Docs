.. sip:method-description::
    :status: todo
    :pysig: 4b2127c7ec4a3dab8a3756cd53b9539a
    :realsig: (const QDateTime&,QTimeZone::NameType,const QLocale&) const
    :digest: e7be25f8eb038d420478d321cd0a32e0

Returns the localized time zone display name.

The name returned is the one for the given *locale*, applicable at the given *atDateTime*, and of the form indicated by *nameType*. The display name may change depending on DST or historical events. If no suitably localized name of the given type is available, another name type may be used, or an empty string may be returned.

If the *locale* is not provided, then the application default locale will be used. For custom timezones created by client code, the data supplied to the constructor are used, as no localization data will be available for it. If this timezone is invalid, an empty string is returned. This may also arise for the representation of local time if determining the system time zone fails.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

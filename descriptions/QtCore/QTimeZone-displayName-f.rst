.. sip:method-description::
    :status: todo
    :pysig: 4b2127c7ec4a3dab8a3756cd53b9539a
    :realsig: (const QDateTime&,QTimeZone::NameType,const QLocale&) const
    :digest: 6b79c9f987a8d289bdf303c19c56d374

Returns the localized time zone display name at the given *atDateTime* for the given *nameType* in the given *locale*. The *nameType* and *locale* requested may not be supported on all platforms, in which case the best available option will be returned.

If the *locale* is not provided then the application default locale will be used.

The display name may change depending on DST or historical events.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

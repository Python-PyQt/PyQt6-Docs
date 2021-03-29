.. sip:method-description::
    :status: todo
    :pysig: 4b2127c7ec4a3dab8a3756cd53b9539a
    :realsig: (const QDateTime&,QTimeZone::NameType,const QLocale&) const
    :digest: c69d5f75591cd56f8387c254bffa948a

Returns the localized time zone display name at the given *atDateTime* for the given *nameType* in the given *locale*. The *nameType* and *locale* requested may not be supported on all platforms, in which case the best available option will be returned.

If the *locale* is not provided then the application default locale will be used.

The display name may change depending on DST or historical events.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

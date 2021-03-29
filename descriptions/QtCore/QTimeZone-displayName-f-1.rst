.. sip:method-description::
    :status: todo
    :pysig: fa76660ed289d70dbd7dba1b5c85cbef
    :realsig: (QTimeZone::TimeType,QTimeZone::NameType,const QLocale&) const
    :digest: be5fbe86225b218b0592d69c712d6837

Returns the localized time zone display name for the given *timeType* and *nameType* in the given *locale*. The *nameType* and *locale* requested may not be supported on all platforms, in which case the best available option will be returned.

If the *locale* is not provided then the application default locale will be used.

Where the time zone display names have changed over time then the most recent names will be used.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`.

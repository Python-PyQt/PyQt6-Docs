.. sip:method-description::
    :status: todo
    :pysig: 818ceb9f7882cf71214966cf00526abf
    :realsig: (QByteArrayView) const
    :digest: f8513393795e0f591fa9d2a652669fb7

Returns ``true`` if *alias* is an alternative name for this timezone.

The IANA (formerly Olson) database has renamed some zones during its history. There are also some zones that only differed prior to 1970 but are now treated as synonymous. Some backends may have data reaching to before 1970 and produce distinct zones in the latter case. Others may produce zones indistinguishable except by :sip:ref:`~PyQt6.QtCore.QTimeZone.id`. This method determines whether an ID refers (at least since 1970) to the same zone that this timezone object describes.

This method is only available when feature ``timezone`` is enabled.

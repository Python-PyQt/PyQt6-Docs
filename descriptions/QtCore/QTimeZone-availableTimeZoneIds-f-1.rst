.. sip:method-description::
    :status: todo
    :pysig: b163d5d22810b836b1eba40f96b816c5
    :realsig: (QLocale::Country)
    :digest: 3f87517c529f1edd0959883236ff394b

Returns a list of all available IANA time zone IDs for a given *country*.

As a special case, a *country* of Qt::AnyCountry returns those time zones that do not have any country related to them, such as UTC. If you require a list of all time zone IDs for all countries then use the standard :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds` method.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable`.

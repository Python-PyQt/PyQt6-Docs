.. sip:method-description::
    :status: todo
    :pysig: 72a8d28079ef10f5bc7cb0c660f97ca7
    :realsig: (const QDateTime&, const QDateTime&) const
    :digest: 1a9b770e0339649cb012817d90925246

Returns a list of all time zone transitions between the given datetimes.

The given *fromDateTime* and *toDateTime* are inclusive. The ``atUtc`` member of each entry describes the moment of the transition, at which the offsets and abbreviation given by other members take effect.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.hasTransitions`, :sip:ref:`~PyQt6.QtCore.QTimeZone.nextTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.previousTransition`.

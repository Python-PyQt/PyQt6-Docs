.. sip:method-description::
    :status: todo
    :pysig: b4a4562e063482e0cc4123384b013e51
    :realsig: (const QDateTime&,const QDateTime&) const
    :digest: 24480e771c402db00fd8508d75a7a237

Returns a list of all time zone transitions between the given datetimes.

The given *fromDateTime* and *toDateTime* are inclusive.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.hasTransitions`, :sip:ref:`~PyQt6.QtCore.QTimeZone.nextTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.previousTransition`.

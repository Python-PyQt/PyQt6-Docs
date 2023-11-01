.. sip:method-description::
    :status: todo
    :pysig: d03de0efeffef2d91ec115e9924b405c
    :realsig: (const QDateTime&) const
    :digest: 2aaf84a8b3ec6566cd280ceee6bfd92f

Returns the first time zone Transition before the given *beforeDateTime*. This is most useful when you have a Transition time and wish to find the Transition before it.

If there is no transition before the given *beforeDateTime* then an invalid :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData` will be returned with an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` as its ``atUtc``.

The given *beforeDateTime* is exclusive.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.hasTransitions`, :sip:ref:`~PyQt6.QtCore.QTimeZone.nextTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.transitions`.

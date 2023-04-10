.. sip:method-description::
    :status: todo
    :pysig: d03de0efeffef2d91ec115e9924b405c
    :realsig: (const QDateTime&) const
    :digest: 59cabc32e9aabda4995b008db0d54dd5

Returns the first time zone Transition after the given *afterDateTime*. This is most useful when you have a Transition time and wish to find the Transition after it.

If there is no transition after the given *afterDateTime* then an invalid :sip:ref:`~PyQt6.QtCore.QTimeZone.OffsetData` will be returned with an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

The given *afterDateTime* is exclusive.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.hasTransitions`, :sip:ref:`~PyQt6.QtCore.QTimeZone.previousTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.transitions`.

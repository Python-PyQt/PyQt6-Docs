.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 02960370cf9c9bddc088bde6bafc6315

Returns ``true`` if the system backend supports obtaining transitions.

Transitions are changes in the time-zone: these happen when DST turns on or off and when authorities alter the offsets for the time-zone.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.nextTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.previousTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.transitions`.

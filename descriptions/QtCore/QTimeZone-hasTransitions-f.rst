.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: dc022133b46c42ba8cbe0df29ef1d35a

Returns ``true`` if the system backend supports obtaining transitions.

Transitions are changes in the time-zone: these happen when DST turns on or off and when authorities alter the offsets for the time-zone.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.nextTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.previousTransition`, :sip:ref:`~PyQt6.QtCore.QTimeZone.transitions`.

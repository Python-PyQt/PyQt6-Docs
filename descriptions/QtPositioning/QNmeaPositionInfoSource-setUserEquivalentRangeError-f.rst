.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (double)
    :digest: 933ccacc5e867098f9c0bc84b078c71c

Sets the User Equivalent Range Error (UERE) to *uere*. The UERE is used in calculating an estimate of the accuracy of the position information reported by the position info source. The UERE should be set to a value appropriate for the GPS device which generated the NMEA stream.

The true UERE value is calculated from multiple error sources including errors introduced by the satellites and signal propogation delays through the atmosphere as well as errors introduced by the receiving GPS equipment. For details on GPS accuracy see `http://edu-observatory.org/gps/gps_accuracy.html <http://edu-observatory.org/gps/gps_accuracy.html>`_.

A typical value for UERE is approximately 5.1.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.userEquivalentRangeError`.

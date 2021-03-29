.. sip:method-description::
    :status: todo
    :pysig: 986b4f3c9e2246f276541e22afe7cbac
    :realsig: ()
    :digest: dfb2bc968c99abc30de5cf227139b685

Returns the current time as reported by the system clock.

Note that the accuracy depends on the accuracy of the underlying operating system; not all systems provide 1-millisecond accuracy.

Furthermore,  only increases within each day; it shall drop by 24 hours each time midnight passes; and, beside this, changes in it may not correspond to elapsed time, if a daylight-saving transition intervenes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.currentDateTime`, :sip:ref:`~PyQt6.QtCore.QDateTime.currentDateTimeUtc`.

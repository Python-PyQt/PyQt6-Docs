.. sip:method-description::
    :status: todo
    :pysig: 14c51f3c39475f1c91fd7d9e1661bc33
    :realsig: (const QMediaTimeRange::Interval&)
    :digest: ce942299606efe941a8a1b13c305e9fb

Adds the specified *interval* to the time range.

Adding intervals which are not :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.Interval.isNormal` is invalid, and will be ignored.

If the specified interval is adjacent to, or overlaps existing intervals within the time range, these intervals will be merged.

This operation takes linear time.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.removeInterval`.

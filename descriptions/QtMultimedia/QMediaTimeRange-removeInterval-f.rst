.. sip:method-description::
    :status: todo
    :pysig: 14c51f3c39475f1c91fd7d9e1661bc33
    :realsig: (const QMediaTimeRange::Interval&)
    :digest: 6fc74813556fbc44617764a640a0add2

Removes the specified *interval* from the time range.

Removing intervals which are not :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.Interval.isNormal` is invalid, and will be ignored.

Intervals within the time range will be trimmed, split or deleted such that no intervals within the time range include any part of the target interval.

This operation takes linear time.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.addInterval`.

.. sip:class-description::
    :status: todo
    :brief: Represents a set of zero or more disjoint time intervals
    :digest: 983d349942cb8048de6a7affac2fd606

The :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange` class represents a set of zero or more disjoint time intervals.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.earliestTime`, :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.latestTime`, :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.intervals` and :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.isEmpty` methods are used to get information about the current time range.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.addInterval`, :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.removeInterval` and :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.clear` methods are used to modify the current time range.

When adding or removing intervals from the time range, existing intervals within the range may be expanded, trimmed, deleted, merged or split to ensure that all intervals within the time range remain distinct and disjoint. As a consequence, all intervals added or removed from a time range must be :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.Interval.isNormal`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange.Interval`.

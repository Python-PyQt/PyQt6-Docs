.. sip:enum-description::
    :status: todo
    :digest: 4b62bf4cd26751e4555fc83bb9e2d48b

This enumeration is used to resolve datetime combinations which fall in :ref:`qdatetime-timezone-transitions`.

When constructing a datetime, specified in terms of local time or a time-zone that has daylight-saving time, or revising one with :sip:ref:`~PyQt6.QtCore.QDateTime.setDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTime` or :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, the given parameters may imply a time representation that either has no meaning or has two meanings in the zone. Such time representations are described as being in the transition. In either case, we can simply return an invalid datetime, to indicate that the operation is ill-defined. In the ambiguous case, we can alternatively select one of the two times that could be meant. When there is no meaning, we can select a time either side of it that might plausibly have been meant. For example, when advancing from an earlier time, we can select the time after the transition that is actually the specified amount of time after the earlier time in question. The options specified here configure how such selection is performed.

For :sip:ref:`~PyQt6.QtCore.QDateTime.addDays`, :sip:ref:`~PyQt6.QtCore.QDateTime.addMonths` or :sip:ref:`~PyQt6.QtCore.QDateTime.addYears`, the behavior is and (mostly) was to use ``RelativeToBefore`` if adding a positive adjustment and ``RelativeToAfter`` if adding a negative adjustment.

**Note:** In time zones where daylight-saving increases the offset from UTC in summer (known as "positive DST"), PreferStandard is an alias for RelativeToAfter and PreferDaylightSaving for RelativeToBefore. In time zones where the daylight-saving mechanism is a decrease in offset from UTC in winter (known as "negative DST"), the reverse applies, provided the operating system reports - as it does on most platforms - whether a datetime is in DST or standard time. For some platforms, where transition times are unavailable even for :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` datetimes, :sip:ref:`~PyQt6.QtCore.QTimeZone` is obliged to presume that the side with lower offset from UTC is standard time, effectively assuming positive DST.

The following tables illustrate how a :sip:ref:`~PyQt6.QtCore.QDateTime` constructor resolves a request for 02:30 on a day when local time has a transition between 02:00 and 03:00, with a nominal standard time LST and daylight-saving time LDT on the two sides, in the various possible cases. The transition type may be to skip an hour or repeat it. The type of transition and value of a parameter ``resolve`` determine which actual time on the given date is selected. First, the common case of positive daylight-saving, where:

+--------+-------------+-------+----------------------+-----------+
| Before | 02:00–03:00 | After | ``resolve``          | selected  |
+========+=============+=======+======================+===========+
| LST    | skip        | LDT   | RelativeToBefore     | 03:30 LDT |
+--------+-------------+-------+----------------------+-----------+
| LST    | skip        | LDT   | RelativeToAfter      | 01:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LST    | skip        | LDT   | PreferBefore         | 01:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LST    | skip        | LDT   | PreferAfter          | 03:30 LDT |
+--------+-------------+-------+----------------------+-----------+
| LST    | skip        | LDT   | PreferStandard       | 01:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LST    | skip        | LDT   | PreferDaylightSaving | 03:30 LDT |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | RelativeToBefore     | 02:30 LDT |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | RelativeToAfter      | 02:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | PreferBefore         | 02:30 LDT |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | PreferAfter          | 02:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | PreferStandard       | 02:30 LST |
+--------+-------------+-------+----------------------+-----------+
| LDT    | repeat      | LST   | PreferDaylightSaving | 02:30 LDT |
+--------+-------------+-------+----------------------+-----------+

Second, the case for negative daylight-saving, using LDT in winter and skipping an hour to transition to LST in summer, then repeating an hour at the transition back to winter:

+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | RelativeToBefore     | 03:30 LST |
+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | RelativeToAfter      | 01:30 LDT |
+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | PreferBefore         | 01:30 LDT |
+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | PreferAfter          | 03:30 LST |
+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | PreferStandard       | 03:30 LST |
+-----+--------+-----+----------------------+-----------+
| LDT | skip   | LST | PreferDaylightSaving | 01:30 LDT |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | RelativeToBefore     | 02:30 LST |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | RelativeToAfter      | 02:30 LDT |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | PreferBefore         | 02:30 LST |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | PreferAfter          | 02:30 LDT |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | PreferStandard       | 02:30 LST |
+-----+--------+-----+----------------------+-----------+
| LST | repeat | LDT | PreferDaylightSaving | 02:30 LDT |
+-----+--------+-----+----------------------+-----------+

Reject can be used to prompt relevant :sip:ref:`~PyQt6.QtCore.QDateTime` APIs to return an invalid datetime object so that your code can deal with transitions for itself, for example by alerting a user to the fact that the datetime they have selected is in a transition interval, to offer them the opportunity to resolve a conflict or ambiguity. Code using this may well find the other options above useful to determine relevant information to use in its own (or the user's) resolution. If the start or end of the transition, or the moment of the transition itself, is the right resolution, :sip:ref:`~PyQt6.QtCore.QTimeZone`'s transition APIs can be used to obtain that information. You can determine whether the transition is a repeated or skipped interval by using :sip:ref:`~PyQt6.QtCore.QDateTime.secsTo` to measure the actual time between noon on the previous and following days. The result will be less than 48 hours for a skipped interval (such as a spring-forward) and more than 48 hours for a repeated interval (such as a fall-back).

**Note:** When a resolution other than Reject is specified, a valid :sip:ref:`~PyQt6.QtCore.QDateTime` object is returned, if possible. If the requested date-time falls in a gap, the returned date-time will not have the :sip:ref:`~PyQt6.QtCore.QDateTime.time` requested - or, in some cases, the :sip:ref:`~PyQt6.QtCore.QDateTime.date`, if a whole day was skipped. You can thus detect when a gap is hit by comparing :sip:ref:`~PyQt6.QtCore.QDateTime.date` and :sip:ref:`~PyQt6.QtCore.QDateTime.time` to what was requested.

Relation to other datetime software
...................................

The Python programming language's datetime APIs have a ``fold`` parameter that corresponds to ``RelativeToBefore`` (``fold = True``) and ``RelativeToAfter`` (``fold = False``).

The ``Temporal`` proposal to replace JavaScript's ``Date`` offers four options for how to resolve a transition, as value for a ``disambiguation`` parameter. Its ``'reject'`` raises an exception, which roughly corresponds to ``Reject`` producing an invalid result. Its ``'earlier'`` and ``'later'`` options correspond to ``PreferBefore`` and ``PreferAfter``. Its ``'compatible'`` option corresponds to ``RelativeToBefore`` (and Python's ``fold = True``).

.. seealso:: :ref:`qdatetime-timezone-transitions`\ .

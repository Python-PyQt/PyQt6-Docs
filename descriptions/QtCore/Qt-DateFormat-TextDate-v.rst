.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: e2404795dd2fdf0c2441d734f4df2553

The default Qt format, which includes the day and month name, the day number in the month, and the year in full. The day and month names will be short names in English (C locale). This effectively uses, for a date, format ``ddd MMM d yyyy``, for a time ``HH:mm:ss`` and combines these as ``ddd MMM d HH:mm:ss yyyy`` for a date-time, with an optional suffix indicating time-zone or offset from UTC, where relevant. A fractional part is also recognized on the seconds of a time part, as ``HH:mm:ss.zzz``, when reading from a string.

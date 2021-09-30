.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 38e0eaa5fef778dca607c48c34873714

The default Qt format, which includes the day and month name, the day number in the month, and the year in full. The day and month names will be short names in English (C locale). This effectively uses, for a date, format ``ddd MMM d yyyy``, for a time ``HH:mm:ss`` and combines these as ``ddd MMM d HH:mm:ss yyyy`` for a date-time, with an optional zone-offset suffix, where relevant. When reading from a string, a fractional part is also recognized on the seconds of a time part, as ``HH:mm:ss.zzz``, and some minor variants on the format may be recognized, for compatibility with earlier versions of Qt and with changes to the format planned for the future. In particular, the zone-offset suffix presently uses ``GMT[±tzoff]`` with a ``tzoff`` in ``HH[[:]mm]`` format (two-digit hour and optional two-digit minutes, with optional colon separator); this shall change to use ``UTC`` in place of ``GMT`` in a future release of Qt, so the planned ``UTC`` format is recognized.

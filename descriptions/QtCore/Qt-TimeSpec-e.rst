.. sip:enum-description::
    :status: todo
    :digest: 43c128dee491e4dc6979a1a36a94d9e9

Both  and  will take care of transitions, such as the start and end of daylight-saving time. UTC is the standard time relative to which time-zones are usually specified: Greenwich Mean Time has zero offset from it. Neither UTC nor  has any transitions.

**Note:** After a change to the system time-zone setting, the behavior of -based :sip:ref:`~PyQt6.QtCore.QDateTime` objects created before the change is undefined: :sip:ref:`~PyQt6.QtCore.QDateTime` may have cached data that the change invalidates. (This is not triggered by transitions of the system time-zone.) In long-running processes, updates to the system's time-zone data (e.g. when politicians change the rules for a zone) may likewise lead to conflicts between the updated time-zone information and data cached by :sip:ref:`~PyQt6.QtCore.QDateTime` objects created before the update, using either  or .

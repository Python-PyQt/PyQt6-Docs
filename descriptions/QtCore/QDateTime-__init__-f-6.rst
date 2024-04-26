.. sip:method-description::
    :status: todo
    :pysig: 213eda8e35d95e27fb0fefa671ebdffa
    :realsig: (QDate, QTime, const QTimeZone&, QDateTime::TransitionResolution)
    :digest: 83451a723a1a63f9d25bbdc9c2270929

Constructs a datetime with the given *date* and *time*, using the time representation described by *timeZone*.

If *date* is valid and *time* is not, the time will be set to midnight. If *timeZone* is invalid then the datetime will be invalid. If *date* and *time* describe a moment close to a transition for *timeZone*, *resolve* controls how that situation is resolved.

**Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

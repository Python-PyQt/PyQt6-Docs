.. sip:method-description::
    :status: todo
    :pysig: 7b30e3c78923008b6da9ef0900e72ef5
    :realsig: (QDate, QTime, QDateTime::TransitionResolution)
    :digest: d2b964c9251a15c9e9aea6a3b701c80b

This is an overloaded function.

Constructs a datetime with the given *date* and *time*, using local time.

If *date* is valid and *time* is not, midnight will be used as the time. If *date* and *time* describe a moment close to a transition for local time, *resolve* controls how that situation is resolved.

**Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

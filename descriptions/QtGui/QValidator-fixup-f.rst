.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (QString&) const
    :digest: 5d6f13545d5a87919435ac323414b2e4

This function attempts to change *input* to be valid according to this validator's rules. It need not result in a valid string: callers of this function must re-test afterwards; the default does nothing.

Reimplementations of this function can change *input* even if they do not produce a valid string. For example, an ISBN validator might want to delete every character except digits and "-", even if the result is still not a valid ISBN; a surname validator might want to remove whitespace from the start and end of the string, even if the resulting string is not in the list of accepted surnames.

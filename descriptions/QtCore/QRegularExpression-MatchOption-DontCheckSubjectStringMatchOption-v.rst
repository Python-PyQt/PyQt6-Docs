.. sip:enum-member-description::
    :status: todo
    :value: 0x0002
    :digest: 5a959c903b9699e9157062c4a6b558e7

The subject string is not checked for UTF-16 validity before attempting a match. Use this option with extreme caution, as attempting to match an invalid string may crash the program and/or constitute a security issue. This enum value has been introduced in Qt 5.4.

.. sip:method-description::
    :status: todo
    :pysig: 574920ad07b505a745cfdb141ecd3aa8
    :realsig: (const QRegularExpression&,QTextDocument::FindFlags)
    :digest: cb3f79bbcf7456ed0a14c5a5abe0fbad

This is an overloaded function.

Finds the next occurrence, matching the regular expression, *exp*, using the given *options*.

Returns ``true`` if a match was found and changes the cursor to select the match; otherwise returns ``false``.

**Warning:** For historical reasons, the case sensitivity option set on *exp* is ignored. Instead, the *options* are used to determine if the search is case sensitive or not.

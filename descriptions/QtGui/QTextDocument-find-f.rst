.. sip:method-description::
    :status: todo
    :pysig: f72f1625a4869a07bfd014dd3889ece7
    :realsig: (const QRegularExpression&,const QTextCursor&,QTextDocument::FindFlags) const
    :digest: 68ab2840f42d6e5edc8ebbbb29ed264f

Finds the next occurrence that matches the given regular expression, *expr*, within the same paragraph in the document.

The search starts at the position of the given *cursor*, and proceeds forwards through the document unless specified otherwise in the search options. The *options* control the type of search performed.

Returns a cursor with the match selected if a match was found; otherwise returns a null cursor.

If the given *cursor* has a selection, the search begins after the selection; otherwise it begins at the cursor's position.

By default the search is case insensitive, and can match text anywhere in the document.

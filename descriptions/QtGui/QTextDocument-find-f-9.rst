.. sip:method-description::
    :status: todo
    :pysig: d8a4798d8a4f1030af0d5fe535993345
    :realsig: (const QString&, int, QTextDocument::FindFlags) const
    :digest: 2aa2b10317a16f26d6cf30dad3f0d497

Finds the next occurrence of the string, *subString*, in the document. The search starts at the given *position*, and proceeds forwards through the document unless specified otherwise in the search options. The *options* control the type of search performed.

Returns a cursor with the match selected if *subString* was found; otherwise returns a null cursor.

If the *position* is 0 (the default) the search begins from the beginning of the document; otherwise it begins at the specified position.

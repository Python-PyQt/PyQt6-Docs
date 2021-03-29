.. sip:method-description::
    :status: todo
    :pysig: ce611ababdd8f6f488f238b7943b6f13
    :realsig: (const QString&,int,QTextDocument::FindFlags) const
    :digest: 74bfc34b65751a01b842be5d82e348e7

This is an overloaded function.

Finds the next occurrence of the string, *subString*, in the document. The search starts at the given *position*, and proceeds forwards through the document unless specified otherwise in the search options. The *options* control the type of search performed.

Returns a cursor with the match selected if *subString* was found; otherwise returns a null cursor.

If the *position* is 0 (the default) the search begins from the beginning of the document; otherwise it begins at the specified position.

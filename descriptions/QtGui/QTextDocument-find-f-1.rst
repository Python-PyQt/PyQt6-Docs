.. sip:method-description::
    :status: todo
    :pysig: d7d9e07f9df1c1143f8ed30ade7871fa
    :realsig: (const QRegularExpression&,int,QTextDocument::FindFlags) const
    :digest: 885e1fcc7ea878df2fc7bf5bbad73b8a

Finds the next occurrence that matches the given regular expression, *expr*, within the same paragraph in the document.

The search starts at the given *from* position, and proceeds forwards through the document unless specified otherwise in the search options. The *options* control the type of search performed.

Returns a cursor with the match selected if a match was found; otherwise returns a null cursor.

If the *from* position is 0 (the default) the search begins from the beginning of the document; otherwise it begins at the specified position.

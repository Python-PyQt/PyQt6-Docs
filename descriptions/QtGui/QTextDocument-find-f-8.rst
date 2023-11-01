.. sip:method-description::
    :status: todo
    :pysig: 4a5f1e3dae3ab9078a230f4e5221a7ff
    :realsig: (const QString&, const QTextCursor&, QTextDocument::FindFlags) const
    :digest: 04fb053460fa36d9f5b30b8e8b38acac

Finds the next occurrence of the string, *subString*, in the document. The search starts at the position of the given *cursor*, and proceeds forwards through the document unless specified otherwise in the search options. The *options* control the type of search performed.

Returns a cursor with the match selected if *subString* was found; otherwise returns a null cursor.

If the given *cursor* has a selection, the search begins after the selection; otherwise it begins at the cursor's position.

By default the search is case insensitive, and can match text anywhere in the document.

.. sip:method-description::
    :status: todo
    :pysig: 690ff780a2b2b089099cc8704f4803c0
    :realsig: (const QUrl&) const
    :digest: 81bae9df785fcfc9c4785507973be0bc

Returns ``true`` if this URL is a parent of *childUrl*. *childUrl* is a child of this URL if the two URLs share the same scheme and authority, and this URL's path is a parent of the path of *childUrl*.

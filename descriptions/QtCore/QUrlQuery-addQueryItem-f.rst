.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&,const QString&)
    :digest: 7822e214a3f68c586892fe33170423b7

Appends the pair *key* = *value* to the end of the query string of the URL. This method does not overwrite existing items that might exist with the same key.

**Note:** This method does not treat spaces (ASCII 0x20) and plus ("+") signs as the same, like HTML forms do. If you need spaces to be represented as plus signs, use actual plus signs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.hasQueryItem`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryItemValue`.

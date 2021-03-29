.. sip:method-description::
    :status: todo
    :pysig: 4b3a6218bb3e3a7303e8a171a60fcf92
    :realsig: ()
    :digest: 695b2187799802709bccf6b25ccbd369

Returns a pointer to the data stored in the byte array. The pointer can be used to access and modify the bytes that compose the array. The data is '\\0'-terminated, i.e. the number of bytes you can access following the returned pointer is :sip:ref:`~PyQt6.QtCore.QByteArray.size` + 1, including the '\\0' terminator.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 128-133

The pointer remains valid as long as no detach happens and the :sip:ref:`~PyQt6.QtCore.QByteArray` is not modified.

For read-only access, constData() is faster because it never causes a `deep copy <https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy>`_ to occur.

This function is mostly useful to pass a byte array to a function that accepts a ``const char \*``.

The following example makes a copy of the char\* returned by , but it will corrupt the heap and cause a crash because it does not allocate a byte for the '\\0' at the end:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 448-452

This one allocates the correct amount of space:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 456-460

Note: A :sip:ref:`~PyQt6.QtCore.QByteArray` can store any byte values including '\\0's, but most functions that take ``char \*`` arguments assume that the data ends at the first '\\0' they encounter.

.. seealso:: constData(), operator[]().

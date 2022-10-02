.. sip:method-description::
    :status: todo
    :pysig: 85614b66e1780877cf0b12760bffaa85
    :realsig: (const QUrl&) const
    :digest: b7b59636e99897d1a77529b0f584f8c7

Returns the result of the merge of this URL with *relative*. This URL is used as a base to convert *relative* to an absolute URL.

If *relative* is not a relative URL, this function will return *relative* directly. Otherwise, the paths of the two URLs are merged, and the new URL returned has the scheme and authority of the base URL, but with the merged path, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 88-91

Calling resolved() with ".." returns a :sip:ref:`~PyQt6.QtCore.QUrl` whose directory is one level higher than the original. Similarly, calling resolved() with "../.." removes two levels from the path. If *relative* is "/", the path becomes "/".

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.isRelative`.

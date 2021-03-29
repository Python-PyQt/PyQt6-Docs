.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 62e8f4cec7feef0a63586fbfd57dee0f

Returns the path of this URL formatted as a local file path. The path returned will use forward slashes, even if it was originally created from one with backslashes.

If this URL contains a non-empty hostname, it will be encoded in the returned value in the form found on SMB networks (for example, "//servername/path/to/file.txt").

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 188-190

Note: if the path component of this URL contains a non-UTF-8 binary sequence (such as %80), the behaviour of this function is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile`, :sip:ref:`~PyQt6.QtCore.QUrl.isLocalFile`.

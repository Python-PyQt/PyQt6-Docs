.. sip:method-description::
    :status: todo
    :pysig: 13af69613e085aff67dd6349f06e8881
    :realsig: (const QString&)
    :digest: 57a578866380806242a32b9fd4be0481

Returns a :sip:ref:`~PyQt6.QtCore.QUrl` representation of *localFile*, interpreted as a local file. This function accepts paths separated by slashes as well as the native separator for this platform.

This function also accepts paths with a doubled leading slash (or backslash) to indicate a remote file, as in "//servername/path/to/file.txt". Note that only certain platforms can actually open this file using :sip:ref:`~PyQt6.QtCore.QFile.open`.

An empty *localFile* leads to an empty URL (since Qt 5.4).

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 162-164

In the first line in snippet above, a file URL is constructed from a local, relative path. A file URL with a relative path only makes sense if there is a base URL to resolve it against. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 168-171

To resolve such a URL, it's necessary to remove the scheme beforehand:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 175-177

For this reason, it is better to use a relative URL (that is, no scheme) for relative file paths:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 181-184

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toLocalFile`, :sip:ref:`~PyQt6.QtCore.QUrl.isLocalFile`, :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators`.

.. sip:method-description::
    :status: todo
    :pysig: 75b41bd8a3b4bb4aa098c1a485c252d8
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: ddebaa7afa5ff0519542b54741502a59

Returns the name of the file, excluding the directory path.

Note that, if this :sip:ref:`~PyQt6.QtCore.QUrl` object is given a path ending in a slash, the name of the file is considered empty.

If the path doesn't contain any slash, it is fully returned as the .

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 102-104

The *options* argument controls how to format the file name component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.path`.

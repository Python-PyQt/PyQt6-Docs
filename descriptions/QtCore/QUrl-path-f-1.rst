.. sip:method-description::
    :status: todo
    :pysig: 95c5a62151d056a62c97d208f5476f2a
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: 6570ab1693b0b7543ca101927348496c

Returns the path of the URL.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 141-143

The *options* argument controls how to format the path component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

Note that :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` may cause data loss if those non-representable sequences are present. It is recommended to use that value when the result will be used in a non-URL context, such as sending to an FTP server.

An example of data loss is when you have non-Unicode percent-encoded sequences and use :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` (the default):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 147-147

In this example, there will be some level of data loss because the ``%FF`` cannot be converted.

Data loss can also occur when the path contains sub-delimiters (such as ``+``):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 151-151

Other decoding examples:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 155-158

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setPath`.

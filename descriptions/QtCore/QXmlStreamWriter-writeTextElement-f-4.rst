.. sip:method-description::
    :status: todo
    :pysig: 4548a82a424de40b70622a91da08ea88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: e1d69c69599ae565d5e0844093d0d446

Writes a text element with *qualifiedName* and *text*.

This is a convenience function equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_xml_qxmlstream.py
    :lines: 67-69

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

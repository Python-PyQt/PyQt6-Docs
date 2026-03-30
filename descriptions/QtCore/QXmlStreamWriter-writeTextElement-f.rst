.. sip:method-description::
    :status: todo
    :pysig: 4dac4e0f9eaceb2a1770767b891ec130
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: e1d69c69599ae565d5e0844093d0d446

Writes a text element with *qualifiedName* and *text*.

This is a convenience function equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_xml_qxmlstream.py
    :lines: 67-69

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

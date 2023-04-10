.. sip:method-description::
    :status: todo
    :pysig: 8f8640c3d3b36433eb5bc5b34ab47591
    :realsig: (QAnyStringView,QAnyStringView,QAnyStringView)
    :digest: 23da02aa536d34e60ca035e997568bb6

Writes a text element with *name*, prefixed for the specified *namespaceUri*, and *text*. If the namespace has not been declared, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it.

This is a convenience function equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_xml_qxmlstream.py
    :lines: 74-76

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

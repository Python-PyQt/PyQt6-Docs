.. sip:method-description::
    :status: todo
    :pysig: 88ef868705cc2335f9e741fe200ba116
    :realsig: (const QString&,const QString&,const QString&)
    :digest: 234d1a2f43bdf2f2ba4ba23a3a99ed3d

Writes a text element with *name*, prefixed for the specified *namespaceUri*, and *text*. If the namespace has not been declared, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it.

This is a convenience function equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_xml_qxmlstream.py
    :lines: 74-76

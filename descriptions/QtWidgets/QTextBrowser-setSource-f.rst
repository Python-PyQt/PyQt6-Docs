.. sip:method-description::
    :status: todo
    :pysig: beb9f0a80020657a3456080624f056aa
    :realsig: (const QUrl&,QTextDocument::ResourceType)
    :digest: d9f3e9e30f127660516c8fe96fcefc91

Attempts to load the document at the given *url* with the specified *type*.

If *type* is :sip:ref:`~PyQt6.QtGui.QTextDocument.ResourceType.UnknownResource` (the default), the document type will be detected: that is, if the url ends with an extension of ``.md``, ``.mkd`` or ``.markdown``, the document will be loaded via :sip:ref:`~PyQt6.QtGui.QTextDocument.setMarkdown`; otherwise it will be loaded via :sip:ref:`~PyQt6.QtGui.QTextDocument.setHtml`. This detection can be bypassed by specifying the *type* explicitly.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.source`.

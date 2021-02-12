.. sip:method-description::
    :status: todo
    :pysig: 0abed0e42de7f89673549cff08bd8ff5
    :realsig: (const QXmlStreamNamespaceDeclaration&)
    :digest: 4840785fdb392431bc49cb6ecf9340e6

Adds an *extraNamespaceDeclaration*. The declaration will be valid for children of the current element, or - should the function be called before any elements are read - for the entire XML document.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceDeclarations`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addExtraNamespaceDeclarations`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.setNamespaceProcessing`.

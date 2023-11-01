.. sip:method-description::
    :status: todo
    :pysig: bd683aa6285abb31767b6eadc947fc23
    :realsig: (const QString&, const QString&, const QString&)
    :digest: cc1cca2a18c942cfc7e12f74af377136

Creates a document type node for the name *qName*.

*publicId* specifies the public identifier of the external subset. If you specify an empty string (QString()) as the *publicId*, this means that the document type has no public identifier.

*systemId* specifies the system identifier of the external subset. If you specify an empty string as the *systemId*, this means that the document type has no system identifier.

Since you cannot have a public identifier without a system identifier, the public identifier is set to an empty string if there is no system identifier.

DOM level 2 does not support any other document type declaration features.

The only way you can use a document type that was created this way, is in combination with the :sip:ref:`~PyQt6.QtXml.QDomImplementation.createDocument` function to create a :sip:ref:`~PyQt6.QtXml.QDomDocument` with this document type.

In the DOM specification, this is the only way to create a non-null document. For historical reasons, Qt also allows to create the document using the default empty constructor. The resulting document is null, but becomes non-null when a factory function, for example :sip:ref:`~PyQt6.QtXml.QDomDocument.createElement`, is called. The document also becomes non-null when setContent() is called.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomImplementation.createDocument`.

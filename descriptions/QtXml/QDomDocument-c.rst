.. sip:class-description::
    :status: todo
    :brief: Represents an XML document
    :digest: 43862a2e2f1ed87e4a5d3080f4709b3f

The :sip:ref:`~PyQt6.QtXml.QDomDocument` class represents an XML document.

The :sip:ref:`~PyQt6.QtXml.QDomDocument` class represents the entire XML document. Conceptually, it is the root of the document tree, and provides the primary access to the document's data.

Since elements, text nodes, comments, processing instructions, etc., cannot exist outside the context of a document, the document class also contains the factory functions needed to create these objects. The node objects created have an ownerDocument() function which associates them with the document within whose context they were created. The DOM classes that will be used most often are :sip:ref:`~PyQt6.QtXml.QDomNode`, :sip:ref:`~PyQt6.QtXml.QDomDocument`, :sip:ref:`~PyQt6.QtXml.QDomElement` and :sip:ref:`~PyQt6.QtXml.QDomText`.

The parsed XML is represented internally by a tree of objects that can be accessed using the various QDom classes. All QDom classes only *reference* objects in the internal tree. The internal objects in the DOM tree will get deleted once the last QDom object referencing them or the :sip:ref:`~PyQt6.QtXml.QDomDocument` itself is deleted.

Creation of elements, text nodes, etc. is done using the various factory functions provided in this class. Using the default constructors of the QDom classes will only result in empty objects that cannot be manipulated or inserted into the Document.

The :sip:ref:`~PyQt6.QtXml.QDomDocument` class has several functions for creating document data, for example, :sip:ref:`~PyQt6.QtXml.QDomDocument.createElement`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createTextNode`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createComment`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createCDATASection`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createProcessingInstruction`, :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttribute` and :sip:ref:`~PyQt6.QtXml.QDomDocument.createEntityReference`. Some of these functions have versions that support namespaces, i.e. :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS` and :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`. The :sip:ref:`~PyQt6.QtXml.QDomDocument.createDocumentFragment` function is used to hold parts of the document; this is useful for manipulating for complex documents.

The entire content of the document is set with :sip:ref:`~PyQt6.QtXml.QDomDocument.setContent`. This function parses the string it is passed as an XML document and creates the DOM tree that represents the document. The root element is available using :sip:ref:`~PyQt6.QtXml.QDomDocument.documentElement`. The textual representation of the document can be obtained using :sip:ref:`~PyQt6.QtXml.QDomDocument.toString`.

**Note:** The DOM tree might end up reserving a lot of memory if the XML document is big. For such documents, the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` or the QXmlQuery classes might be better solutions.

It is possible to insert a node from another document into the document using :sip:ref:`~PyQt6.QtXml.QDomDocument.importNode`.

You can obtain a list of all the elements that have a particular tag with :sip:ref:`~PyQt6.QtXml.QDomDocument.elementsByTagName` or with :sip:ref:`~PyQt6.QtXml.QDomDocument.elementsByTagNameNS`.

The QDom classes are typically used as follows:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom.py
    :lines: 156-182

Once ``doc`` and ``elem`` go out of scope, the whole internal tree representing the XML document is deleted.

To create a document using DOM use code like this:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom.py
    :lines: 189-199

For further information about the Document Object Model see the Document Object Model (DOM) `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_ Specifications.

.. seealso:: `DOM Bookmarks Example <https://doc.qt.io/qt-6/qtxml-dombookmarks-example.html>`_, `Simple DOM Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-simpledommodel-example.html>`_.

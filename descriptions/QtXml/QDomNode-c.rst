.. sip:class-description::
    :status: todo
    :brief: The base class for all the nodes in a DOM tree
    :digest: 3d786a4ec8a5f4bc2a8be0db8b9e59d4

The :sip:ref:`~PyQt6.QtXml.QDomNode` class is the base class for all the nodes in a DOM tree.

Many functions in the DOM return a :sip:ref:`~PyQt6.QtXml.QDomNode`.

You can find out the type of a node using :sip:ref:`~PyQt6.QtXml.QDomNode.isAttr`, :sip:ref:`~PyQt6.QtXml.QDomNode.isCDATASection`, :sip:ref:`~PyQt6.QtXml.QDomNode.isDocumentFragment`, :sip:ref:`~PyQt6.QtXml.QDomNode.isDocument`, :sip:ref:`~PyQt6.QtXml.QDomNode.isDocumentType`, :sip:ref:`~PyQt6.QtXml.QDomNode.isElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.isEntityReference`, :sip:ref:`~PyQt6.QtXml.QDomNode.isText`, :sip:ref:`~PyQt6.QtXml.QDomNode.isEntity`, :sip:ref:`~PyQt6.QtXml.QDomNode.isNotation`, :sip:ref:`~PyQt6.QtXml.QDomNode.isProcessingInstruction`, :sip:ref:`~PyQt6.QtXml.QDomNode.isCharacterData` and :sip:ref:`~PyQt6.QtXml.QDomNode.isComment`.

A :sip:ref:`~PyQt6.QtXml.QDomNode` can be converted into one of its subclasses using :sip:ref:`~PyQt6.QtXml.QDomNode.toAttr`, :sip:ref:`~PyQt6.QtXml.QDomNode.toCDATASection`, :sip:ref:`~PyQt6.QtXml.QDomNode.toDocumentFragment`, :sip:ref:`~PyQt6.QtXml.QDomNode.toDocument`, :sip:ref:`~PyQt6.QtXml.QDomNode.toDocumentType`, :sip:ref:`~PyQt6.QtXml.QDomNode.toElement`, :sip:ref:`~PyQt6.QtXml.QDomNode.toEntityReference`, :sip:ref:`~PyQt6.QtXml.QDomNode.toText`, :sip:ref:`~PyQt6.QtXml.QDomNode.toEntity`, :sip:ref:`~PyQt6.QtXml.QDomNode.toNotation`, :sip:ref:`~PyQt6.QtXml.QDomNode.toProcessingInstruction`, :sip:ref:`~PyQt6.QtXml.QDomNode.toCharacterData` or :sip:ref:`~PyQt6.QtXml.QDomNode.toComment`. You can convert a node to a null node with :sip:ref:`~PyQt6.QtXml.QDomNode.clear`.

Copies of the :sip:ref:`~PyQt6.QtXml.QDomNode` class share their data using explicit sharing. This means that modifying one node will change all copies. This is especially useful in combination with functions which return a :sip:ref:`~PyQt6.QtXml.QDomNode`, e.g. :sip:ref:`~PyQt6.QtXml.QDomNode.firstChild`. You can make an independent (deep) copy of the node with :sip:ref:`~PyQt6.QtXml.QDomNode.cloneNode`.

A :sip:ref:`~PyQt6.QtXml.QDomNode` can be null, much like ``nullptr``. Creating a copy of a null node results in another null node. It is not possible to modify a null node, but it is possible to assign another, possibly non-null node to it. In this case, the copy of the null node will remain null. You can check if a :sip:ref:`~PyQt6.QtXml.QDomNode` is null by calling :sip:ref:`~PyQt6.QtXml.QDomNode.isNull`. The empty constructor of a :sip:ref:`~PyQt6.QtXml.QDomNode` (or any of the derived classes) creates a null node.

Nodes are inserted with :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter` or :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`. You can replace one node with another using :sip:ref:`~PyQt6.QtXml.QDomNode.replaceChild` and remove a node with :sip:ref:`~PyQt6.QtXml.QDomNode.removeChild`.

To traverse nodes use :sip:ref:`~PyQt6.QtXml.QDomNode.firstChild` to get a node's first child (if any), and :sip:ref:`~PyQt6.QtXml.QDomNode.nextSibling` to traverse. :sip:ref:`~PyQt6.QtXml.QDomNode` also provides :sip:ref:`~PyQt6.QtXml.QDomNode.lastChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.previousSibling` and :sip:ref:`~PyQt6.QtXml.QDomNode.parentNode`. To find the first child node with a particular node name use :sip:ref:`~PyQt6.QtXml.QDomNode.namedItem`.

To find out if a node has children use :sip:ref:`~PyQt6.QtXml.QDomNode.hasChildNodes` and to get a list of all of a node's children use :sip:ref:`~PyQt6.QtXml.QDomNode.childNodes`.

The node's name and value (the meaning of which varies depending on its type) is returned by :sip:ref:`~PyQt6.QtXml.QDomNode.nodeName` and :sip:ref:`~PyQt6.QtXml.QDomNode.nodeValue` respectively. The node's type is returned by :sip:ref:`~PyQt6.QtXml.QDomNode.nodeType`. The node's value can be set with :sip:ref:`~PyQt6.QtXml.QDomNode.setNodeValue`.

The document to which the node belongs is returned by :sip:ref:`~PyQt6.QtXml.QDomNode.ownerDocument`.

Adjacent :sip:ref:`~PyQt6.QtXml.QDomText` nodes can be merged into a single node with :sip:ref:`~PyQt6.QtXml.QDomNode.normalize`.

:sip:ref:`~PyQt6.QtXml.QDomElement` nodes have attributes which can be retrieved with :sip:ref:`~PyQt6.QtXml.QDomNode.attributes`.

:sip:ref:`~PyQt6.QtXml.QDomElement` and :sip:ref:`~PyQt6.QtXml.QDomAttr` nodes can have namespaces which can be retrieved with :sip:ref:`~PyQt6.QtXml.QDomNode.namespaceURI`. Their local name is retrieved with :sip:ref:`~PyQt6.QtXml.QDomNode.localName`, and their prefix with :sip:ref:`~PyQt6.QtXml.QDomNode.prefix`. The prefix can be set with :sip:ref:`~PyQt6.QtXml.QDomNode.setPrefix`.

You can write the XML representation of the node to a text stream with :sip:ref:`~PyQt6.QtXml.QDomNode.save`.

The following example looks for the first element in an XML document and prints the names of all the elements that are its direct children.

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom.py
    :lines: 89-101

For further information about the Document Object Model see `Level 1 <https://doc.qt.io/qt-6/http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <https://doc.qt.io/qt-6/http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

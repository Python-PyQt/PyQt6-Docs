.. sip:class-description::
    :status: todo
    :brief: Represents one element in the DOM tree
    :digest: 49766b40d2d67d55437cb920905c8a39

The :sip:ref:`~PyQt6.QtXml.QDomElement` class represents one element in the DOM tree.

Elements have a :sip:ref:`~PyQt6.QtXml.QDomElement.tagName` and zero or more attributes associated with them. The tag name can be changed with :sip:ref:`~PyQt6.QtXml.QDomElement.setTagName`.

Element attributes are represented by :sip:ref:`~PyQt6.QtXml.QDomAttr` objects that can be queried using the :sip:ref:`~PyQt6.QtXml.QDomElement.attribute` and :sip:ref:`~PyQt6.QtXml.QDomElement.attributeNode` functions. You can set attributes with the :sip:ref:`~PyQt6.QtXml.QDomElement.setAttribute` and :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNode` functions. Attributes can be removed with :sip:ref:`~PyQt6.QtXml.QDomElement.removeAttribute`. There are namespace-aware equivalents to these functions, i.e. :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNS`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNodeNS` and :sip:ref:`~PyQt6.QtXml.QDomElement.removeAttributeNS`.

If you want to access the text of a node use :sip:ref:`~PyQt6.QtXml.QDomElement.text`, e.g.

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 76-78

The :sip:ref:`~PyQt6.QtXml.QDomElement.text` function operates recursively to find the text (since not all elements contain text). If you want to find all the text in all of a node's children, iterate over the children looking for :sip:ref:`~PyQt6.QtXml.QDomText` nodes, e.g.

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom.py
    :lines: 130-137

Note that we attempt to convert each node to a text node and use :sip:ref:`~PyQt6.QtXml.QDomElement.text` rather than using firstChild().toText().data() or n.toText().data() directly on the node, because the node may not be a text element.

You can get a list of all the decendents of an element which have a specified tag name with :sip:ref:`~PyQt6.QtXml.QDomElement.elementsByTagName` or :sip:ref:`~PyQt6.QtXml.QDomElement.elementsByTagNameNS`.

To browse the elements of a dom document use firstChildElement(), lastChildElement(), nextSiblingElement() and previousSiblingElement(). For example, to iterate over all child elements called "entry" in a root element called "database", you can use:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 82-87

For further information about the Document Object Model see `Level 1 <https://doc.qt.io/qt-6/http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <https://doc.qt.io/qt-6/http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

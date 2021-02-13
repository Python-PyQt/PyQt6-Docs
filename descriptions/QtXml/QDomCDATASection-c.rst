.. sip:class-description::
    :status: todo
    :brief: Represents an XML CDATA section
    :digest: 2c0595edc9492335d0789202fe37bc97

The :sip:ref:`~PyQt6.QtXml.QDomCDATASection` class represents an XML CDATA section.

CDATA sections are used to escape blocks of text containing characters that would otherwise be regarded as markup. The only delimiter that is recognized in a CDATA section is the "]]&gt;" string that terminates the CDATA section. CDATA sections cannot be nested. Their primary purpose is for including material such as XML fragments, without needing to escape all the delimiters.

Adjacent :sip:ref:`~PyQt6.QtXml.QDomCDATASection` nodes are not merged by the :sip:ref:`~PyQt6.QtXml.QDomNode.normalize` function.

For further information about the Document Object Model see `http://www.w3.org/TR/REC-DOM-Level-1/ <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `http://www.w3.org/TR/DOM-Level-2-Core/ <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

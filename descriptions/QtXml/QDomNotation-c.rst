.. sip:class-description::
    :status: todo
    :brief: Represents an XML notation
    :digest: 602af02d4e96d23e9e9f203b60434f3c

The :sip:ref:`~PyQt6.QtXml.QDomNotation` class represents an XML notation.

A notation either declares, by name, the format of an unparsed entity (see section 4.7 of the XML 1.0 specification), or is used for formal declaration of processing instruction targets (see section 2.6 of the XML 1.0 specification).

DOM does not support editing notation nodes; they are therefore read-only.

A notation node does not have any parent.

You can retrieve the :sip:ref:`~PyQt6.QtXml.QDomNotation.publicId` and :sip:ref:`~PyQt6.QtXml.QDomNotation.systemId` from a notation node.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

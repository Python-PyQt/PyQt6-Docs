.. sip:class-description::
    :status: todo
    :brief: Represents an XML processing instruction
    :digest: c4b4b9b71278db0632a79cd1b6dfdb7c

The :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction` class represents an XML processing instruction.

Processing instructions are used in XML to keep processor-specific information in the text of the document.

The XML declaration that appears at the top of an XML document, typically ``<?xml version='1.0' encoding='UTF-8'?>``, is treated by QDom as a processing instruction. This is unfortunate, since the XML declaration is not a processing instruction; among other differences, it cannot be inserted into a document anywhere but on the first line.

Do not use this function to create an xml declaration, since although it has the same syntax as a processing instruction, it isn't, and might not be treated by QDom as such.

The content of the processing instruction is retrieved with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.data` and set with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.setData`. The processing instruction's target is retrieved with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.target`.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

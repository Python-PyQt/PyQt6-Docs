.. sip:class-description::
    :status: todo
    :brief: Represents an XML processing instruction
    :digest: 3563d018f965dcea972c76347a776aa6

The :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction` class represents an XML processing instruction.

Processing instructions are used in XML to keep processor-specific information in the text of the document.

The XML declaration that appears at the top of an XML document, typically ``<?xml version='1.0' encoding='UTF-8'?>``, is treated by QDom as a processing instruction. This is unfortunate, since the XML declaration is not a processing instruction; among other differences, it cannot be inserted into a document anywhere but on the first line.

**Note:** Do not use this function to create an XML declaration. Although the XML declaration shares the same syntax as a processing instruction, it is not one. According to the `XML 1.0 Specification <https://www.w3.org/TR/xml/#sec-prolog-dtd>`_ and the `W3C DOM Structure Model <https://www.w3.org/TR/REC-DOM-Level-1/level-one-core.html#ID-1590626202>`_, the XML declaration is part of the document prolog and not part of the DOM tree - meaning it should not be represented as a DOM node and cannot be created or inserted via the DOM API. If you need to generate a well-formed XML document that includes an XML declaration, use :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter`, which provides proper support for writing the declaration through :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartDocument`.

The content of the processing instruction is retrieved with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.data` and set with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.setData`. The processing instruction's target is retrieved with :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction.target`.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

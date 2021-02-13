.. sip:class-description::
    :status: todo
    :brief: List of QDomNode objects
    :digest: 40884117da5f6e3ad788f854c859e9f1

The :sip:ref:`~PyQt6.QtXml.QDomNodeList` class is a list of :sip:ref:`~PyQt6.QtXml.QDomNode` objects.

Lists can be obtained by :sip:ref:`~PyQt6.QtXml.QDomDocument.elementsByTagName` and :sip:ref:`~PyQt6.QtXml.QDomNode.childNodes`. The Document Object Model (DOM) requires these lists to be "live": whenever you change the underlying document, the contents of the list will get updated.

You can get a particular node from the list with :sip:ref:`~PyQt6.QtXml.QDomNodeList.item`. The number of items in the list is returned by :sip:ref:`~PyQt6.QtXml.QDomNodeList.length`.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.childNodes`, :sip:ref:`~PyQt6.QtXml.QDomDocument.elementsByTagName`.

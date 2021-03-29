.. sip:class-description::
    :status: todo
    :brief: Tree of QDomNodes which is not usually a complete QDomDocument
    :digest: ceec64555c929e3cf2dd1a28f16db489

The :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment` class is a tree of QDomNodes which is not usually a complete :sip:ref:`~PyQt6.QtXml.QDomDocument`.

If you want to do complex tree operations it is useful to have a lightweight class to store nodes and their relations. :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment` stores a subtree of a document which does not necessarily represent a well-formed XML document.

:sip:ref:`~PyQt6.QtXml.QDomDocumentFragment` is also useful if you want to group several nodes in a list and insert them all together as children of some node. In these cases :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment` can be used as a temporary container for this list of children.

The most important feature of :sip:ref:`~PyQt6.QtXml.QDomDocumentFragment` is that it is treated in a special way by :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.replaceChild` and :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`: instead of inserting the fragment itself, all the fragment's children are inserted.

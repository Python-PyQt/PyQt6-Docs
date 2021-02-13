.. sip:class-description::
    :status: todo
    :brief: Represents an XML entity
    :digest: eb1becc4d3dabac93b8c31ac64dac0e2

The :sip:ref:`~PyQt6.QtXml.QDomEntity` class represents an XML entity.

This class represents an entity in an XML document, either parsed or unparsed. Note that this models the entity itself not the entity declaration.

DOM does not support editing entity nodes; if a user wants to make changes to the contents of an entity, every related :sip:ref:`~PyQt6.QtXml.QDomEntityReference` node must be replaced in the DOM tree by a clone of the entity's contents, and then the desired changes must be made to each of the clones instead. All the descendants of an entity node are read-only.

An entity node does not have any parent.

You can access the entity's :sip:ref:`~PyQt6.QtXml.QDomEntity.publicId`, :sip:ref:`~PyQt6.QtXml.QDomEntity.systemId` and :sip:ref:`~PyQt6.QtXml.QDomEntity.notationName` when available.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

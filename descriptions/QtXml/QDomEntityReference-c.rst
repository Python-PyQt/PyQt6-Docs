.. sip:class-description::
    :status: todo
    :brief: Represents an XML entity reference
    :digest: 1ed5696fe673a22f46d1f26251260c9e

The :sip:ref:`~PyQt6.QtXml.QDomEntityReference` class represents an XML entity reference.

A :sip:ref:`~PyQt6.QtXml.QDomEntityReference` object may be inserted into the DOM tree when an entity reference is in the source document, or when the user wishes to insert an entity reference.

Note that character references and references to predefined entities are expanded by the XML processor so that characters are represented by their Unicode equivalent rather than by an entity reference.

Moreover, the XML processor may completely expand references to entities while building the DOM tree, instead of providing :sip:ref:`~PyQt6.QtXml.QDomEntityReference` objects.

If it does provide such objects, then for a given entity reference node, it may be that there is no entity node representing the referenced entity; but if such an entity exists, then the child list of the entity reference node is the same as that of the entity node. As with the entity node, all descendants of the entity reference are read-only.

For further information about the Document Object Model see `Level 1 <http://www.w3.org/TR/REC-DOM-Level-1/>`_ and `Level 2 Core <http://www.w3.org/TR/DOM-Level-2-Core/>`_. For a more general introduction of the DOM implementation see the :sip:ref:`~PyQt6.QtXml.QDomDocument` documentation.

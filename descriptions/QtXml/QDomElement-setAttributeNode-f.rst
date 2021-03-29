.. sip:method-description::
    :status: todo
    :pysig: 2813106aae49175122856911ac4b2f7e
    :realsig: (const QDomAttr&)
    :digest: 5a54f2fa690de636ee1133bb51ba041a

Adds the attribute *newAttr* to this element.

If the element has another attribute that has the same name as *newAttr*, this function replaces that attribute and returns it; otherwise the function returns a :sip:ref:`~PyQt6.QtXml.QDomNode.isNull`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomElement.attributeNode`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttribute`, :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNodeNS`.

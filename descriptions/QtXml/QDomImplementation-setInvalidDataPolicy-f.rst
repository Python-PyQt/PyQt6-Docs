.. sip:method-description::
    :status: todo
    :pysig: c473660042457ec1a6b912410342ff82
    :realsig: (QDomImplementation::InvalidDataPolicy)
    :digest: 8612b1fb938776c5eb161d9df808f189

Sets the invalid data policy, which specifies what should be done when a factory function in :sip:ref:`~PyQt6.QtXml.QDomDocument` is passed invalid data.

The *policy* is set for all instances of :sip:ref:`~PyQt6.QtXml.QDomDocument` which already exist and which will be created in the future.

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom.py
    :lines: 67-83

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomImplementation.invalidDataPolicy`, :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy.InvalidDataPolicy`.

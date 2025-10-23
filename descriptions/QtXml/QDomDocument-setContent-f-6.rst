.. sip:method-description::
    :status: todo
    :pysig: d087a656bdc7fb0440f70e7089d71d1a
    :realsig: (QXmlStreamReader*,bool,QString*,int*,int*)
    :digest: a7660c9ef72db7089c9c657307973b03

Use the overload taking ParseOptions instead.

This function reads the XML document from the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` *reader* and parses it. Returns ``true`` if the content was successfully parsed; otherwise returns ``false``.

If *namespaceProcessing* is ``true``, the parser recognizes namespaces in the XML file and sets the prefix name, local name and namespace URI to appropriate values. If *namespaceProcessing* is ``false``, the parser does no namespace processing when it reads the XML file.

If a parse error occurs, the error message is placed in ``\*``\ *errorMsg*, the line number in ``\*``\ *errorLine* and the column number in ``\*``\ *errorColumn* (unless the associated pointer is set to ``nullptr``).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`.

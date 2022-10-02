.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: cb2d9d010d12b7b83e329fb3c95b5470

Returns the element's text or an empty string.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 95-95

The function text() of the :sip:ref:`~PyQt6.QtXml.QDomElement` for the ``<h1>`` tag, will return the following text:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 99-99

Comments are ignored by this function. It only evaluates :sip:ref:`~PyQt6.QtXml.QDomText` and :sip:ref:`~PyQt6.QtXml.QDomCDATASection` objects.

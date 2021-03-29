.. sip:method-description::
    :status: todo
    :pysig: 6f9bd443efc69d5fb85e04b6ca205057
    :realsig: () const
    :digest: 50d7f0c323a0fb3c4a3f2eea1869334d

Returns the next sibling in the document tree. Changing the returned node will also change the node in the document tree.

If you have XML like this:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 66-68

and this :sip:ref:`~PyQt6.QtXml.QDomNode` represents the <p> tag,  will return the node representing the <h2> tag.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.previousSibling`.

.. sip:method-description::
    :status: todo
    :pysig: 6f9bd443efc69d5fb85e04b6ca205057
    :realsig: () const
    :digest: cdbe16b11766f10e1f51c89a3d3ad100

Returns the previous sibling in the document tree. Changing the returned node will also change the node in the document tree.

For example, if you have XML like this:

.. literalinclude:: ../../../snippets/qtbase-src-xml-doc-snippets-code-src_xml_dom_qdom_snippet.py
    :lines: 60-62

and this :sip:ref:`~PyQt6.QtXml.QDomNode` represents the &lt;p&gt; tag,  will return the node representing the &lt;h1&gt; tag.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.nextSibling`.

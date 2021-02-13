.. sip:method-description::
    :status: todo
    :pysig: 0497dff377470027a0d7806a80460b5f
    :realsig: (int) const
    :digest: 01718a34dcc428ae0676032bdb8e7fb1

Returns the node at position *index*.

If *index* is negative or if *index* >= :sip:ref:`~PyQt6.QtXml.QDomNodeList.length` then a null node is returned (i.e. a node for which :sip:ref:`~PyQt6.QtXml.QDomNode.isNull` returns true).

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNodeList.length`.

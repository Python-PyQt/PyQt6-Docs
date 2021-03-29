.. sip:method-description::
    :status: todo
    :pysig: 2cd345409a8dd30d3bff69f9f4b4a6c1
    :realsig: (bool) const
    :digest: 5ec268a2c97954ebb750ef8176e58da6

Creates a deep (not shallow) copy of the :sip:ref:`~PyQt6.QtXml.QDomNode`.

If *deep* is true, then the cloning is done recursively which means that all the node's children are deep copied too. If *deep* is false only the node itself is copied and the copy will have no child nodes.

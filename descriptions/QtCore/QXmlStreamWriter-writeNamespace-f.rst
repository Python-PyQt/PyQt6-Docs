.. sip:method-description::
    :status: todo
    :pysig: 5d7c101f9d654b3ba05f3f92783395fb
    :realsig: (const QString&,const QString&)
    :digest: 0bb7103efe1e675c6f1c99e16236f33f

Writes a namespace declaration for *namespaceUri* with *prefix*. If *prefix* is empty, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` assigns a unique prefix consisting of the letter 'n' followed by a number.

If :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` or :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement` was called, the declaration applies to the current element; otherwise it applies to the next child element.

Note that the prefix *xml* is both predefined and reserved for *http://www.w3.org/XML/1998/namespace*, which in turn cannot be bound to any other prefix. The prefix *xmlns* and its URI *http://www.w3.org/2000/xmlns/* are used for the namespace mechanism itself and thus completely forbidden in declarations.

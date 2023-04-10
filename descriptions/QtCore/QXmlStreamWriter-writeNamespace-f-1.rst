.. sip:method-description::
    :status: todo
    :pysig: 593928b172712789f2f69a791bdf47f3
    :realsig: (QAnyStringView,QAnyStringView)
    :digest: 9942e95b0dcfad44ff8c318e940a23bb

Writes a namespace declaration for *namespaceUri* with *prefix*. If *prefix* is empty, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` assigns a unique prefix consisting of the letter 'n' followed by a number.

If :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` or :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement` was called, the declaration applies to the current element; otherwise it applies to the next child element.

Note that the prefix *xml* is both predefined and reserved for *http://www.w3.org/XML/1998/namespace*, which in turn cannot be bound to any other prefix. The prefix *xmlns* and its URI *http://www.w3.org/2000/xmlns/* are used for the namespace mechanism itself and thus completely forbidden in declarations.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

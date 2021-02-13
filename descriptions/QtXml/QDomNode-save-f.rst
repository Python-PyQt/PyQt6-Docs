.. sip:method-description::
    :status: todo
    :pysig: a865483209fe9f25541edc9f5251e7b8
    :realsig: (QTextStream&,int,QDomNode::EncodingPolicy) const
    :digest: 902d8a1a76ead3da2d5bdf82774d6f1b

Writes the XML representation of the node and all its children to the stream *stream*. This function uses *indent* as the amount of space to indent the node.

If the document contains invalid XML characters or characters that cannot be encoded in the given encoding, the result and behavior is undefined.

If *encodingPolicy* is :sip:ref:`~PyQt6.QtXml.QDomNode.EncodingPolicy.EncodingFromDocument` and this node is a document node, the encoding of text stream *stream*'s encoding is set by treating a processing instruction by name "xml" as an XML declaration, if one exists, and otherwise defaults to UTF-8. XML declarations are not processing instructions, but this behavior exists for historical reasons. If this node is not a document node, the text stream's encoding is used.

If *encodingPolicy* is :sip:ref:`~PyQt6.QtXml.QDomNode.EncodingPolicy.EncodingFromTextStream` and this node is a document node, this function behaves as save(\ :sip:ref:`~PyQt6.QtCore.QTextStream` &str, int indent) with the exception that the encoding specified in the text stream *stream* is used.

If the document contains invalid XML characters or characters that cannot be encoded in the given encoding, the result and behavior is undefined.

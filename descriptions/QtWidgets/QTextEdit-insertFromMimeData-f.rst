.. sip:method-description::
    :status: todo
    :pysig: 770e1785bf230215c95e86b61944a276
    :realsig: (const QMimeData*)
    :digest: 657a0cc5573a349684a1ce9bbe094a64

This function inserts the contents of the MIME data object, specified by *source*, into the text edit at the current cursor position. It is called whenever text is inserted as the result of a clipboard paste operation, or when the text edit accepts data from a drag and drop operation.

Reimplement this function to enable drag and drop support for additional MIME types.

.. sip:method-description::
    :status: todo
    :pysig: 6b9963865ea057d7c35dc4d7158a2b41
    :realsig: (QTextInlineObject,int,const QTextFormat&)
    :digest: d9006452baf17a95fad8d0a2da4eebfe

Sets the size of the inline object *item* corresponding to the text *format*.

*posInDocument* specifies the position of the object within the document.

The default implementation resizes the *item* to the size returned by the object handler's intrinsicSize() function. This function is called only within Qt. Subclasses can reimplement this function to customize the resizing of inline objects.

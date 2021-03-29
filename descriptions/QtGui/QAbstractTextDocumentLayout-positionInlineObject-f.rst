.. sip:method-description::
    :status: todo
    :pysig: 6b9963865ea057d7c35dc4d7158a2b41
    :realsig: (QTextInlineObject,int,const QTextFormat&)
    :digest: 45c17176cac35d1a60bcbe2584352763

Lays out the inline object *item* using the given text *format*.

*posInDocument* specifies the position of the object within the document.

The default implementation does nothing. This function is called only within Qt. Subclasses can reimplement this function to customize the position of inline objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.drawInlineObject`.

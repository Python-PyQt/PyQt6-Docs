.. sip:method-description::
    :status: todo
    :pysig: 34aba96fbb180336cdc25075082b0a06
    :realsig: (QPainter*,const QRectF&,QTextInlineObject,int,const QTextFormat&)
    :digest: c64548e763afeb2a497aafbc2ae2d280

This function is called to draw the inline object, *object*, with the given *painter* within the rectangle specified by *rect* using the specified text *format*.

*posInDocument* specifies the position of the object within the document.

The default implementation calls drawObject() on the object handlers. This function is called only within Qt. Subclasses can reimplement this function to customize the drawing of inline objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.draw`.

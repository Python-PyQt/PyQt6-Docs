.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: d2f4ee1c11b938668c79e50430119399

Returns the content's origin in viewport coordinates.

The origin of the content of a plain text edit is always the top left corner of the first visible text block. The content offset is different from (0,0) when the text has been scrolled horizontally, or when the first visible block has been scrolled partially off the screen, i.e. the visible text does not start with the first line of the first visible block, or when the first visible block is the very first block and the editor displays a margin.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.firstVisibleBlock`, horizontalScrollBar(), verticalScrollBar().

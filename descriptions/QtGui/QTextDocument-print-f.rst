.. sip:method-description::
    :status: todo
    :pysig: 09e78aedc17e6d6fc25c58b2f862a648
    :realsig: (QPagedPaintDevice*) const
    :digest: be12ade307a47bb3ceee4b8789074a47

Prints the document to the given *printer*. The :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice` must be set up before being used with this function.

This is only a convenience method to print the whole document to the printer.

If the document is already paginated through a specified height in the :sip:ref:`~PyQt6.QtGui.QTextDocument.pageSize` property it is printed as-is.

If the document is not paginated, like for example a document used in a :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, then a temporary copy of the document is created and the copy is broken into multiple pages according to the size of the paint device's paperRect(). By default a 2 cm margin is set around the document contents. In addition the current page number is printed at the bottom of each page.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit.print`.

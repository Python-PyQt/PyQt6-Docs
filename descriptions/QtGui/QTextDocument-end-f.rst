.. sip:method-description::
    :status: todo
    :pysig: 16811274a5cf1699065413f00eb8108d
    :realsig: () const
    :digest: c2ec9a962f8b91c13c521c243ed63a84

This function returns a block to test for the end of the document while iterating over it.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-end-textdocumentendsnippet.py
    :lines: 63-64

The block returned is invalid and represents the block after the last block in the document. You can use :sip:ref:`~PyQt6.QtGui.QTextDocument.lastBlock` to retrieve the last valid block of the document.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.lastBlock`.

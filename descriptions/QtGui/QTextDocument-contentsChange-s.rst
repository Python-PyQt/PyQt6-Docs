.. sip:signal-description::
    :status: todo
    :pysig: 883579c2ad1a92ea9bbe04c13915d560
    :realsig: (int,int,int)
    :digest: e617e14f5163a89b926efa84c05f8734

This signal is emitted whenever the document's content changes; for example, when text is inserted or deleted, or when formatting is applied.

Information is provided about the *position* of the character in the document where the change occurred, the number of characters removed (\ *charsRemoved*), and the number of characters added (\ *charsAdded*).

The signal is emitted before the document's layout manager is notified about the change. This hook allows you to implement syntax highlighting for the document.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.documentChanged`, :sip:ref:`~PyQt6.QtGui.QTextDocument.contentsChanged`.

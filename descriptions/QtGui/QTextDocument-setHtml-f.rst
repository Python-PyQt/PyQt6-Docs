.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: d664d5702ab4c1e4c8f3d80cd6658fa2

Replaces the entire contents of the document with the given HTML-formatted text in the *html* string. The undo/redo history is reset when this function is called.

The HTML formatting is respected as much as possible; for example, "<b>bold</b> text" will produce text where the first word has a font weight that gives it a bold appearance: "\ **bold** text".

**Note:** It is the responsibility of the caller to make sure that the text is correctly decoded when a QString containing HTML is created and passed to .

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.setPlainText`, `Supported HTML Subset <https://doc.qt.io/qt-6/richtext-html-subset.html>`_.

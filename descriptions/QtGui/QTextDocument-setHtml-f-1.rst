.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 2fe14cf59ee4dc4f85c85b5d38af677e

Replaces the entire contents of the document with the given HTML-formatted text in the *html* string. The undo/redo history is reset when this function is called.

The HTML formatting is respected as much as possible; for example, "<b>bold</b> text" will produce text where the first word has a font weight that gives it a bold appearance: "\ **bold** text".

To select a css media rule other than the default "screen" rule, use :sip:ref:`~PyQt6.QtGui.QTextDocument.setMetaInformation` with '\ :sip:ref:`~PyQt6.QtGui.QTextDocument.MetaInformation.CssMedia`' as "info" parameter.

**Note:** It is the responsibility of the caller to make sure that the text is correctly decoded when a QString containing HTML is created and passed to setHtml().

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.setPlainText`, `Supported HTML Subset <https://doc.qt.io/qt-6/richtext-html-subset.html>`_, :sip:ref:`~PyQt6.QtGui.QTextDocument.setMetaInformation`.

.. sip:method-description::
    :status: todo
    :pysig: b8143efd05f0edbea3429f39921ff8af
    :realsig: (const QString&, QTextDocument::MarkdownFeatures)
    :digest: 508cf46cffa407986e43d50b233aad70

Returns a :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` based on the given *markdown* text with the specified *features*. The default is GitHub dialect.

The formatting is preserved as much as possible; for example, ``\*\*bold\*\*`` will become a document fragment containing the text "bold" with a bold character style.

**Note:** Loading external resources is not supported.

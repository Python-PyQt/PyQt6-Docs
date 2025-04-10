.. sip:method-description::
    :status: todo
    :pysig: f42b2afdc10729cd99a2122e09d76453
    :realsig: (const QString&, QTextDocument::MarkdownFeatures)
    :digest: bfcaddc8ebcbc67642ca83ae0f76004b

Replaces the entire contents of the document with the given Markdown-formatted text in the *markdown* string, with the given *features* supported. By default, all supported GitHub-style Markdown features are included; pass ``MarkdownDialectCommonMark`` for a more basic parse.

The Markdown formatting is respected as much as possible; for example, "\*bold\* text" will produce text where the first word has a font weight that gives it an emphasized appearance.

Parsing of HTML included in the *markdown* string is handled in the same way as in :sip:ref:`~PyQt6.QtGui.QTextDocument.setHtml`; however, Markdown formatting inside HTML blocks is not supported.

Some features of the parser can be enabled or disabled via the *features* argument. The default is ``MarkdownDialectGitHub``.

The undo/redo history is reset when this function is called.

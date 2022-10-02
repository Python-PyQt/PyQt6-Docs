.. sip:class-description::
    :status: todo
    :brief: Represents a piece of formatted text from a QTextDocument
    :digest: cff66e07b610b7d8366ce3559aa8a5fa

The :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` class represents a piece of formatted text from a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` is a fragment of rich text, that can be inserted into a :sip:ref:`~PyQt6.QtGui.QTextDocument`. A document fragment can be created from a :sip:ref:`~PyQt6.QtGui.QTextDocument`, from a :sip:ref:`~PyQt6.QtGui.QTextCursor`'s selection, or from another document fragment. Document fragments can also be created by the static functions, :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.fromPlainText` and :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.fromHtml`.

The contents of a document fragment can be obtained as raw text by using the :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toRawText` function, as ASCII with :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toPlainText`, as HTML with :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toHtml`, or as Markdown with :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toMarkdown`.

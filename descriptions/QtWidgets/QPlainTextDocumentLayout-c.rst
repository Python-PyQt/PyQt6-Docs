.. sip:class-description::
    :status: todo
    :brief: Implements a plain text layout for QTextDocument
    :digest: 6ce700737ba90cfc623f832f9aa1bf24

The :sip:ref:`~PyQt6.QtWidgets.QPlainTextDocumentLayout` class implements a plain text layout for :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A :sip:ref:`~PyQt6.QtWidgets.QPlainTextDocumentLayout` is required for text documents that can be display or edited in a :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit`. See :sip:ref:`~PyQt6.QtGui.QTextDocument.setDocumentLayout`.

:sip:ref:`~PyQt6.QtWidgets.QPlainTextDocumentLayout` uses the :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` API that :sip:ref:`~PyQt6.QtGui.QTextDocument` requires, but redefines it partially in order to support plain text better. For instances, it does not operate on vertical pixels, but on paragraphs (called blocks) instead. The height of a document is identical to the number of paragraphs it contains. The layout also doesn't support tables or nested frames, or any sort of advanced text layout that goes beyond a list of paragraphs with syntax highlighting.

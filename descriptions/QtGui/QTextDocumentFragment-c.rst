.. sip:class-description::
    :status: todo
    :brief: Represents a piece of formatted text from a QTextDocument
    :digest: cbb060b6aa61bb769a635e14fcd7fe05

The :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` class represents a piece of formatted text from a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment` is a fragment of rich text, that can be inserted into a :sip:ref:`~PyQt6.QtGui.QTextDocument`. A document fragment can be created from a :sip:ref:`~PyQt6.QtGui.QTextDocument`, from a :sip:ref:`~PyQt6.QtGui.QTextCursor`'s selection, or from another document fragment. Document fragments can also be created by the static functions, :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.fromPlainText` and :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.fromHtml`.

The contents of a document fragment can be obtained as plain text by using the :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toPlainText` function, or it can be obtained as HTML with :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toHtml`.

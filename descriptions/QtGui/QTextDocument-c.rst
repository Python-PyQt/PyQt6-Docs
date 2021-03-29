.. sip:class-description::
    :status: todo
    :brief: Holds formatted text
    :digest: f79c71c9f29126a8c38fd29cf7ebb2fc

The :sip:ref:`~PyQt6.QtGui.QTextDocument` class holds formatted text.

:sip:ref:`~PyQt6.QtGui.QTextDocument` is a container for structured rich text documents, providing support for styled text and various types of document elements, such as lists, tables, frames, and images. They can be created for use in a :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, or used independently.

Each document element is described by an associated format object. Each format object is treated as a unique object by QTextDocuments, and can be passed to :sip:ref:`~PyQt6.QtGui.QTextDocument.objectForFormat` to obtain the document element that it is applied to.

A :sip:ref:`~PyQt6.QtGui.QTextDocument` can be edited programmatically using a :sip:ref:`~PyQt6.QtGui.QTextCursor`, and its contents can be examined by traversing the document structure. The entire document structure is stored as a hierarchy of document elements beneath the root frame, found with the :sip:ref:`~PyQt6.QtGui.QTextDocument.rootFrame` function. Alternatively, if you just want to iterate over the textual contents of the document you can use :sip:ref:`~PyQt6.QtGui.QTextDocument.begin`, :sip:ref:`~PyQt6.QtGui.QTextDocument.end`, and :sip:ref:`~PyQt6.QtGui.QTextDocument.findBlock` to retrieve text blocks that you can examine and iterate over.

The layout of a document is determined by the :sip:ref:`~PyQt6.QtGui.QTextDocument.documentLayout`; you can create your own :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` subclass and set it using :sip:ref:`~PyQt6.QtGui.QTextDocument.setDocumentLayout` if you want to use your own layout logic. The document's title and other meta-information can be obtained by calling the :sip:ref:`~PyQt6.QtGui.QTextDocument.metaInformation` function. For documents that are exposed to users through the :sip:ref:`~PyQt6.QtWidgets.QTextEdit` class, the document title is also available via the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.documentTitle` function.

The :sip:ref:`~PyQt6.QtGui.QTextDocument.toPlainText` and :sip:ref:`~PyQt6.QtGui.QTextDocument.toHtml` convenience functions allow you to retrieve the contents of the document as plain text and HTML. The document's text can be searched using the :sip:ref:`~PyQt6.QtGui.QTextDocument.find` functions.

Undo/redo of operations performed on the document can be controlled using the :sip:ref:`~PyQt6.QtGui.QTextDocument.setUndoRedoEnabled` function. The undo/redo system can be controlled by an editor widget through the :sip:ref:`~PyQt6.QtGui.QTextDocument.undo` and :sip:ref:`~PyQt6.QtGui.QTextDocument.redo` slots; the document also provides :sip:ref:`~PyQt6.QtGui.QTextDocument.contentsChanged`, :sip:ref:`~PyQt6.QtGui.QTextDocument.undoAvailable`, and :sip:ref:`~PyQt6.QtGui.QTextDocument.redoAvailable` signals that inform connected editor widgets about the state of the undo/redo system. The following are the undo/redo operations of a :sip:ref:`~PyQt6.QtGui.QTextDocument`:

* Insertion or removal of characters. A sequence of insertions or removals within the same text block are regarded as a single undo/redo operation.

* Insertion or removal of text blocks. Sequences of insertion or removals in a single operation (e.g., by selecting and then deleting text) are regarded as a single undo/redo operation.

* Text character format changes.

* Text block format changes.

* Text block group format changes.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, `Rich Text Processing <https://doc.qt.io/qt-6/richtext.html>`_, `Text Object Example <https://doc.qt.io/qt-6/qtsvg-richtext-textobject-example.html>`_.

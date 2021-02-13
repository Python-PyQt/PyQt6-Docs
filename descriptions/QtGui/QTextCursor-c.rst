.. sip:class-description::
    :status: todo
    :brief: Offers an API to access and modify QTextDocuments
    :digest: 6102caecdb8fff0f19e57d94d58e2a7a

The :sip:ref:`~PyQt6.QtGui.QTextCursor` class offers an API to access and modify QTextDocuments.

Text cursors are objects that are used to access and modify the contents and underlying structure of text documents via a programming interface that mimics the behavior of a cursor in a text editor. :sip:ref:`~PyQt6.QtGui.QTextCursor` contains information about both the cursor's position within a :sip:ref:`~PyQt6.QtGui.QTextDocument` and any selection that it has made.

:sip:ref:`~PyQt6.QtGui.QTextCursor` is modeled on the way a text cursor behaves in a text editor, providing a programmatic means of performing standard actions through the user interface. A document can be thought of as a single string of characters. The cursor's current :sip:ref:`~PyQt6.QtGui.QTextCursor.position` then is always either *between* two consecutive characters in the string, or else *before* the very first character or *after* the very last character in the string. Documents can also contain tables, lists, images, and other objects in addition to text but, from the developer's point of view, the document can be treated as one long string. Some portions of that string can be considered to lie within particular blocks (e.g. paragraphs), or within a table's cell, or a list's item, or other structural elements. When we refer to "current character" we mean the character immediately *before* the cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position` in the document. Similarly, the "current block" is the block that contains the cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position`.

A :sip:ref:`~PyQt6.QtGui.QTextCursor` also has an :sip:ref:`~PyQt6.QtGui.QTextCursor.anchor` position. The text that is between the :sip:ref:`~PyQt6.QtGui.QTextCursor.anchor` and the :sip:ref:`~PyQt6.QtGui.QTextCursor.position` is the selection. If :sip:ref:`~PyQt6.QtGui.QTextCursor.anchor` == :sip:ref:`~PyQt6.QtGui.QTextCursor.position` there is no selection.

The cursor position can be changed programmatically using :sip:ref:`~PyQt6.QtGui.QTextCursor.setPosition` and :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition`; the latter can also be used to select text. For selections see :sip:ref:`~PyQt6.QtGui.QTextCursor.selectionStart`, :sip:ref:`~PyQt6.QtGui.QTextCursor.selectionEnd`, :sip:ref:`~PyQt6.QtGui.QTextCursor.hasSelection`, :sip:ref:`~PyQt6.QtGui.QTextCursor.clearSelection`, and :sip:ref:`~PyQt6.QtGui.QTextCursor.removeSelectedText`.

If the :sip:ref:`~PyQt6.QtGui.QTextCursor.position` is at the start of a block, :sip:ref:`~PyQt6.QtGui.QTextCursor.atBlockStart` returns ``true``; and if it is at the end of a block, :sip:ref:`~PyQt6.QtGui.QTextCursor.atBlockEnd` returns true. The format of the current character is returned by :sip:ref:`~PyQt6.QtGui.QTextCursor.charFormat`, and the format of the current block is returned by :sip:ref:`~PyQt6.QtGui.QTextCursor.blockFormat`.

Formatting can be applied to the current text document using the :sip:ref:`~PyQt6.QtGui.QTextCursor.setCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextCursor.mergeCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextCursor.setBlockFormat` and :sip:ref:`~PyQt6.QtGui.QTextCursor.mergeBlockFormat` functions. The 'set' functions will replace the cursor's current character or block format, while the 'merge' functions add the given format properties to the cursor's current format. If the cursor has a selection, the given format is applied to the current selection. Note that when only a part of a block is selected, the block format is applied to the entire block. The text at the current character position can be turned into a list using :sip:ref:`~PyQt6.QtGui.QTextCursor.createList`.

Deletions can be achieved using :sip:ref:`~PyQt6.QtGui.QTextCursor.deleteChar`, :sip:ref:`~PyQt6.QtGui.QTextCursor.deletePreviousChar`, and :sip:ref:`~PyQt6.QtGui.QTextCursor.removeSelectedText`.

Text strings can be inserted into the document with the :sip:ref:`~PyQt6.QtGui.QTextCursor.insertText` function, blocks (representing new paragraphs) can be inserted with :sip:ref:`~PyQt6.QtGui.QTextCursor.insertBlock`.

Existing fragments of text can be inserted with :sip:ref:`~PyQt6.QtGui.QTextCursor.insertFragment` but, if you want to insert pieces of text in various formats, it is usually still easier to use :sip:ref:`~PyQt6.QtGui.QTextCursor.insertText` and supply a character format.

Various types of higher-level structure can also be inserted into the document with the cursor:

* Lists are ordered sequences of block elements that are decorated with bullet points or symbols. These are inserted in a specified format with :sip:ref:`~PyQt6.QtGui.QTextCursor.insertList`.

* Tables are inserted with the :sip:ref:`~PyQt6.QtGui.QTextCursor.insertTable` function, and can be given an optional format. These contain an array of cells that can be traversed using the cursor.

* Inline images are inserted with :sip:ref:`~PyQt6.QtGui.QTextCursor.insertImage`. The image to be used can be specified in an image format, or by name.

* Frames are inserted by calling :sip:ref:`~PyQt6.QtGui.QTextCursor.insertFrame` with a specified format.

Actions can be grouped (i.e. treated as a single action for undo/redo) using :sip:ref:`~PyQt6.QtGui.QTextCursor.beginEditBlock` and :sip:ref:`~PyQt6.QtGui.QTextCursor.endEditBlock`.

Cursor movements are limited to valid cursor positions. In Latin writing this is between any two consecutive characters in the text, before the first character, or after the last character. In some other writing systems cursor movements are limited to "clusters" (e.g. a syllable in Devanagari, or a base letter plus diacritics). Functions such as :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition` and :sip:ref:`~PyQt6.QtGui.QTextCursor.deleteChar` limit cursor movement to these valid positions.

.. seealso:: `Rich Text Processing <https://doc.qt.io/qt-6/richtext.html>`_.

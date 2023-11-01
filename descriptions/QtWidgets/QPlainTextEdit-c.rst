.. sip:class-description::
    :status: todo
    :brief: Widget that is used to edit and display plain text
    :digest: e16da538a3b6af5156de01763367bf93

The :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` class provides a widget that is used to edit and display plain text.

.. _qplaintextedit-introduction-and-concepts:

Introduction and Concepts
-------------------------

:sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` is an advanced viewer/editor supporting plain text. It is optimized to handle large documents and to respond quickly to user input.

QPlainText uses very much the same technology and concepts as :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, but is optimized for plain text handling.

:sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` works on paragraphs and characters. A paragraph is a formatted string which is word-wrapped to fit into the width of the widget. By default when reading plain text, one newline signifies a paragraph. A document consists of zero or more paragraphs. Paragraphs are separated by hard line breaks. Each character within a paragraph has its own attributes, for example, font and color.

The shape of the mouse cursor on a :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` is :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.IBeamCursor` by default. It can be changed through the viewport()'s cursor property.

.. _qplaintextedit-using-qplaintextedit-as-a-display-widget:

Using QPlainTextEdit as a Display Widget
----------------------------------------

The text is set or replaced using :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setPlainText` which deletes the existing text and replaces it with the text passed to :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setPlainText`.

Text can be inserted using the :sip:ref:`~PyQt6.QtGui.QTextCursor` class or using the convenience functions :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.insertPlainText`, :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.appendPlainText` or :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.paste`.

By default, the text edit wraps words at whitespace to fit within the text edit widget. The :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setLineWrapMode` function is used to specify the kind of line wrap you want, :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth` or :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap` if you don't want any wrapping. If you use word wrap to the widget's width :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth`, you can specify whether to break on whitespace or anywhere with :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setWordWrapMode`.

The :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.find` function can be used to find and select a given string within the text.

If you want to limit the total number of paragraphs in a :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit`, as it is for example useful in a log viewer, then you can use the :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.maximumBlockCount` property. The combination of :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setMaximumBlockCount` and :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.appendPlainText` turns :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` into an efficient viewer for log text. The scrolling can be reduced with the :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.centerOnScroll` property, making the log viewer even faster. Text can be formatted in a limited way, either using a syntax highlighter (see below), or by appending html-formatted text with :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.appendHtml`. While :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` does not support complex rich text rendering with tables and floats, it does support limited paragraph-based formatting that you may need in a log viewer.

.. _qplaintextedit-read-only-key-bindings:

Read-only Key Bindings
......................

When :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` is used read-only the key bindings are limited to navigation, and text may only be selected with the mouse:

+--------------------------------------------------+---------------------------------------------------------------+
| Keypresses                                       | Action                                                        |
+==================================================+===============================================================+
| :sip:ref:`~PyQt6.QtCore.Qt.ArrowType.UpArrow`    | Moves one line up.                                            |
+--------------------------------------------------+---------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ArrowType.DownArrow`  | Moves one line down.                                          |
+--------------------------------------------------+---------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ArrowType.LeftArrow`  | Moves one character to the left.                              |
+--------------------------------------------------+---------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ArrowType.RightArrow` | Moves one character to the right.                             |
+--------------------------------------------------+---------------------------------------------------------------+
| PageUp                                           | Moves one (viewport) page up.                                 |
+--------------------------------------------------+---------------------------------------------------------------+
| PageDown                                         | Moves one (viewport) page down.                               |
+--------------------------------------------------+---------------------------------------------------------------+
| Home                                             | Moves to the beginning of the text.                           |
+--------------------------------------------------+---------------------------------------------------------------+
| End                                              | Moves to the end of the text.                                 |
+--------------------------------------------------+---------------------------------------------------------------+
| Alt+Wheel                                        | Scrolls the page horizontally (the Wheel is the mouse wheel). |
+--------------------------------------------------+---------------------------------------------------------------+
| Ctrl+Wheel                                       | Zooms the text.                                               |
+--------------------------------------------------+---------------------------------------------------------------+
| Ctrl+A                                           | Selects all text.                                             |
+--------------------------------------------------+---------------------------------------------------------------+

.. _qplaintextedit-using-qplaintextedit-as-an-editor:

Using QPlainTextEdit as an Editor
---------------------------------

All the information about using :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` as a display widget also applies here.

Selection of text is handled by the :sip:ref:`~PyQt6.QtGui.QTextCursor` class, which provides functionality for creating selections, retrieving the text contents or deleting selections. You can retrieve the object that corresponds with the user-visible cursor using the :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.textCursor` method. If you want to set a selection in :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` just create one on a :sip:ref:`~PyQt6.QtGui.QTextCursor` object and then make that cursor the visible cursor using setCursor(). The selection can be copied to the clipboard with :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.copy`, or cut to the clipboard with :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.cut`. The entire text can be selected using :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.selectAll`.

:sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` holds a :sip:ref:`~PyQt6.QtGui.QTextDocument` object which can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.document` method. You can also set your own document object using :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setDocument`. :sip:ref:`~PyQt6.QtGui.QTextDocument` emits a :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.textChanged` signal if the text changes and it also provides a isModified() function which will return true if the text has been modified since it was either loaded or since the last call to setModified with false as argument. In addition it provides methods for undo and redo.

.. _qplaintextedit-syntax-highlighting:

Syntax Highlighting
...................

Just like :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` works together with :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter`.

.. _qplaintextedit-editing-key-bindings:

Editing Key Bindings
....................

The list of key bindings which are implemented for editing:

+-----------------+---------------------------------------------------------------+
| Keypresses      | Action                                                        |
+=================+===============================================================+
| Backspace       | Deletes the character to the left of the cursor.              |
+-----------------+---------------------------------------------------------------+
| Delete          | Deletes the character to the right of the cursor.             |
+-----------------+---------------------------------------------------------------+
| Ctrl+C          | Copy the selected text to the clipboard.                      |
+-----------------+---------------------------------------------------------------+
| Ctrl+Insert     | Copy the selected text to the clipboard.                      |
+-----------------+---------------------------------------------------------------+
| Ctrl+K          | Deletes to the end of the line.                               |
+-----------------+---------------------------------------------------------------+
| Ctrl+V          | Pastes the clipboard text into text edit.                     |
+-----------------+---------------------------------------------------------------+
| Shift+Insert    | Pastes the clipboard text into text edit.                     |
+-----------------+---------------------------------------------------------------+
| Ctrl+X          | Deletes the selected text and copies it to the clipboard.     |
+-----------------+---------------------------------------------------------------+
| Shift+Delete    | Deletes the selected text and copies it to the clipboard.     |
+-----------------+---------------------------------------------------------------+
| Ctrl+Z          | Undoes the last operation.                                    |
+-----------------+---------------------------------------------------------------+
| Ctrl+Y          | Redoes the last operation.                                    |
+-----------------+---------------------------------------------------------------+
| LeftArrow       | Moves the cursor one character to the left.                   |
+-----------------+---------------------------------------------------------------+
| Ctrl+LeftArrow  | Moves the cursor one word to the left.                        |
+-----------------+---------------------------------------------------------------+
| RightArrow      | Moves the cursor one character to the right.                  |
+-----------------+---------------------------------------------------------------+
| Ctrl+RightArrow | Moves the cursor one word to the right.                       |
+-----------------+---------------------------------------------------------------+
| UpArrow         | Moves the cursor one line up.                                 |
+-----------------+---------------------------------------------------------------+
| Ctrl+UpArrow    | Moves the cursor one word up.                                 |
+-----------------+---------------------------------------------------------------+
| DownArrow       | Moves the cursor one line down.                               |
+-----------------+---------------------------------------------------------------+
| Ctrl+Down Arrow | Moves the cursor one word down.                               |
+-----------------+---------------------------------------------------------------+
| PageUp          | Moves the cursor one page up.                                 |
+-----------------+---------------------------------------------------------------+
| PageDown        | Moves the cursor one page down.                               |
+-----------------+---------------------------------------------------------------+
| Home            | Moves the cursor to the beginning of the line.                |
+-----------------+---------------------------------------------------------------+
| Ctrl+Home       | Moves the cursor to the beginning of the text.                |
+-----------------+---------------------------------------------------------------+
| End             | Moves the cursor to the end of the line.                      |
+-----------------+---------------------------------------------------------------+
| Ctrl+End        | Moves the cursor to the end of the text.                      |
+-----------------+---------------------------------------------------------------+
| Alt+Wheel       | Scrolls the page horizontally (the Wheel is the mouse wheel). |
+-----------------+---------------------------------------------------------------+
| Ctrl+Wheel      | Zooms the text.                                               |
+-----------------+---------------------------------------------------------------+

To select (mark) text hold down the Shift key whilst pressing one of the movement keystrokes, for example, *Shift+Right Arrow* will select the character to the right, and *Shift+Ctrl+Right Arrow* will select the word to the right, etc.

.. _qplaintextedit-differences-to-qtextedit:

Differences to QTextEdit
------------------------

:sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` is a thin class, implemented by using most of the technology that is behind :sip:ref:`~PyQt6.QtWidgets.QTextEdit` and :sip:ref:`~PyQt6.QtGui.QTextDocument`. Its performance benefits over :sip:ref:`~PyQt6.QtWidgets.QTextEdit` stem mostly from using a different and simplified text layout called :sip:ref:`~PyQt6.QtWidgets.QPlainTextDocumentLayout` on the text document (see :sip:ref:`~PyQt6.QtGui.QTextDocument.setDocumentLayout`). The plain text document layout does not support tables nor embedded frames, and *replaces a pixel-exact height calculation with a line-by-line respectively paragraph-by-paragraph scrolling approach*. This makes it possible to handle significantly larger documents, and still resize the editor with line wrap enabled in real time. It also makes for a fast log viewer (see :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.setMaximumBlockCount`).

{Syntax Highlighter Example}, {Rich Text Processing}

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument`, :sip:ref:`~PyQt6.QtGui.QTextCursor`.

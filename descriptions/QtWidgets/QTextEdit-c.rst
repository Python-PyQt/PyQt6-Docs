.. sip:class-description::
    :status: todo
    :brief: Widget that is used to edit and display both plain and rich text
    :digest: e2ba3839f1d9e60f1e43b911135a2f0a

The :sip:ref:`~PyQt6.QtWidgets.QTextEdit` class provides a widget that is used to edit and display both plain and rich text.

.. _qtextedit-introduction-and-concepts:

Introduction and Concepts
-------------------------

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` is an advanced WYSIWYG viewer/editor supporting rich text formatting using HTML-style tags, or Markdown format. It is optimized to handle large documents and to respond quickly to user input.

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` works on paragraphs and characters. A paragraph is a formatted string which is word-wrapped to fit into the width of the widget. By default when reading plain text, one newline signifies a paragraph. A document consists of zero or more paragraphs. The words in the paragraph are aligned in accordance with the paragraph's alignment. Paragraphs are separated by hard line breaks. Each character within a paragraph has its own attributes, for example, font and color.

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` can display images, lists and tables. If the text is too large to view within the text edit's viewport, scroll bars will appear. The text edit can load both plain text and rich text files. Rich text can be described using a subset of HTML 4 markup; refer to the `Supported HTML Subset <https://doc.qt.io/qt-6/richtext-html-subset.html>`_ page for more information.

If you just need to display a small piece of rich text use :sip:ref:`~PyQt6.QtWidgets.QLabel`.

The rich text support in Qt is designed to provide a fast, portable and efficient way to add reasonable online help facilities to applications, and to provide a basis for rich text editors. If you find the HTML support insufficient for your needs you may consider the use of Qt WebKit, which provides a full-featured web browser widget.

The shape of the mouse cursor on a :sip:ref:`~PyQt6.QtWidgets.QTextEdit` is :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.IBeamCursor` by default. It can be changed through the viewport()'s cursor property.

.. _qtextedit-using-qtextedit-as-a-display-widget:

Using QTextEdit as a Display Widget
-----------------------------------

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` can display a large HTML subset, including tables and images.

The text can be set or replaced using :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setHtml` which deletes any existing text and replaces it with the text passed in the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setHtml` call. If you call :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setHtml` with legacy HTML, and then call :sip:ref:`~PyQt6.QtWidgets.QTextEdit.toHtml`, the text that is returned may have different markup, but will render the same. The entire text can be deleted with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.clear`.

Text can also be set or replaced using :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setMarkdown`, and the same caveats apply: if you then call :sip:ref:`~PyQt6.QtWidgets.QTextEdit.toMarkdown`, the text that is returned may be different, but the meaning is preserved as much as possible. Markdown with some embedded HTML can be parsed, with the same limitations that :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setHtml` has; but :sip:ref:`~PyQt6.QtWidgets.QTextEdit.toMarkdown` only writes "pure" Markdown, without any embedded HTML.

Text itself can be inserted using the :sip:ref:`~PyQt6.QtGui.QTextCursor` class or using the convenience functions :sip:ref:`~PyQt6.QtWidgets.QTextEdit.insertHtml`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.insertPlainText`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.append` or :sip:ref:`~PyQt6.QtWidgets.QTextEdit.paste`. :sip:ref:`~PyQt6.QtGui.QTextCursor` is also able to insert complex objects like tables or lists into the document, and it deals with creating selections and applying changes to selected text.

By default the text edit wraps words at whitespace to fit within the text edit widget. The :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setLineWrapMode` function is used to specify the kind of line wrap you want, or :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode.NoWrap` if you don't want any wrapping. Call :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setLineWrapMode` to set a fixed pixel width :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode.FixedPixelWidth`, or character column (e.g. 80 column) :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode.FixedColumnWidth` with the pixels or columns specified with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setLineWrapColumnOrWidth`. If you use word wrap to the widget's width :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode.WidgetWidth`, you can specify whether to break on whitespace or anywhere with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setWordWrapMode`.

The :sip:ref:`~PyQt6.QtWidgets.QTextEdit.find` function can be used to find and select a given string within the text.

If you want to limit the total number of paragraphs in a :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, as for example it is often useful in a log viewer, then you can use :sip:ref:`~PyQt6.QtGui.QTextDocument`'s maximumBlockCount property for that.

.. _qtextedit-read-only-key-bindings:

Read-only Key Bindings
......................

When :sip:ref:`~PyQt6.QtWidgets.QTextEdit` is used read-only the key bindings are limited to navigation, and text may only be selected with the mouse:

+------------+---------------------------------------------------------------+
| Keypresses | Action                                                        |
+============+===============================================================+
| Up         | Moves one line up.                                            |
+------------+---------------------------------------------------------------+
| Down       | Moves one line down.                                          |
+------------+---------------------------------------------------------------+
| Left       | Moves one character to the left.                              |
+------------+---------------------------------------------------------------+
| Right      | Moves one character to the right.                             |
+------------+---------------------------------------------------------------+
| PageUp     | Moves one (viewport) page up.                                 |
+------------+---------------------------------------------------------------+
| PageDown   | Moves one (viewport) page down.                               |
+------------+---------------------------------------------------------------+
| Home       | Moves to the beginning of the text.                           |
+------------+---------------------------------------------------------------+
| End        | Moves to the end of the text.                                 |
+------------+---------------------------------------------------------------+
| Alt+Wheel  | Scrolls the page horizontally (the Wheel is the mouse wheel). |
+------------+---------------------------------------------------------------+
| Ctrl+Wheel | Zooms the text.                                               |
+------------+---------------------------------------------------------------+
| Ctrl+A     | Selects all text.                                             |
+------------+---------------------------------------------------------------+

The text edit may be able to provide some meta-information. For example, the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.documentTitle` function will return the text from within HTML ``<title>`` tags.

**Note:** Zooming into HTML documents only works if the font-size is not set to a fixed size.

.. _qtextedit-using-qtextedit-as-an-editor:

Using QTextEdit as an Editor
----------------------------

All the information about using :sip:ref:`~PyQt6.QtWidgets.QTextEdit` as a display widget also applies here.

The current char format's attributes are set with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setFontItalic`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setFontWeight`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setFontUnderline`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setFontFamily`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setFontPointSize`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setTextColor` and :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setCurrentFont`. The current paragraph's alignment is set with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setAlignment`.

Selection of text is handled by the :sip:ref:`~PyQt6.QtGui.QTextCursor` class, which provides functionality for creating selections, retrieving the text contents or deleting selections. You can retrieve the object that corresponds with the user-visible cursor using the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.textCursor` method. If you want to set a selection in :sip:ref:`~PyQt6.QtWidgets.QTextEdit` just create one on a :sip:ref:`~PyQt6.QtGui.QTextCursor` object and then make that cursor the visible cursor using :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setTextCursor`. The selection can be copied to the clipboard with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.copy`, or cut to the clipboard with :sip:ref:`~PyQt6.QtWidgets.QTextEdit.cut`. The entire text can be selected using :sip:ref:`~PyQt6.QtWidgets.QTextEdit.selectAll`.

When the cursor is moved and the underlying formatting attributes change, the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.currentCharFormatChanged` signal is emitted to reflect the new attributes at the new cursor position.

The :sip:ref:`~PyQt6.QtWidgets.QTextEdit.textChanged` signal is emitted whenever the text changes (as a result of :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setText` or through the editor itself).

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` holds a :sip:ref:`~PyQt6.QtGui.QTextDocument` object which can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.document` method. You can also set your own document object using :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setDocument`.

:sip:ref:`~PyQt6.QtGui.QTextDocument` provides an :sip:ref:`~PyQt6.QtGui.QTextDocument.isModified` function which will return true if the text has been modified since it was either loaded or since the last call to setModified with false as argument. In addition it provides methods for undo and redo.

.. _qtextedit-drag-and-drop:

Drag and Drop
.............

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` also supports custom drag and drop behavior. By default, :sip:ref:`~PyQt6.QtWidgets.QTextEdit` will insert plain text, HTML and rich text when the user drops data of these MIME types onto a document. Reimplement :sip:ref:`~PyQt6.QtWidgets.QTextEdit.canInsertFromMimeData` and :sip:ref:`~PyQt6.QtWidgets.QTextEdit.insertFromMimeData` to add support for additional MIME types.

For example, to allow the user to drag and drop an image onto a :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, you could the implement these functions in the following way:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-textdocument-imagedrop-textedit.py
    :lines: 62-68

We add support for image MIME types by returning true. For all other MIME types, we use the default implementation.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-textdocument-imagedrop-textedit.py
    :lines: 72-82

We unpack the image from the `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ held by the MIME source and insert it into the document as a resource.

.. _qtextedit-editing-key-bindings:

Editing Key Bindings
....................

The list of key bindings which are implemented for editing:

+--------------+---------------------------------------------------------------+
| Keypresses   | Action                                                        |
+==============+===============================================================+
| Backspace    | Deletes the character to the left of the cursor.              |
+--------------+---------------------------------------------------------------+
| Delete       | Deletes the character to the right of the cursor.             |
+--------------+---------------------------------------------------------------+
| Ctrl+C       | Copy the selected text to the clipboard.                      |
+--------------+---------------------------------------------------------------+
| Ctrl+Insert  | Copy the selected text to the clipboard.                      |
+--------------+---------------------------------------------------------------+
| Ctrl+K       | Deletes to the end of the line.                               |
+--------------+---------------------------------------------------------------+
| Ctrl+V       | Pastes the clipboard text into text edit.                     |
+--------------+---------------------------------------------------------------+
| Shift+Insert | Pastes the clipboard text into text edit.                     |
+--------------+---------------------------------------------------------------+
| Ctrl+X       | Deletes the selected text and copies it to the clipboard.     |
+--------------+---------------------------------------------------------------+
| Shift+Delete | Deletes the selected text and copies it to the clipboard.     |
+--------------+---------------------------------------------------------------+
| Ctrl+Z       | Undoes the last operation.                                    |
+--------------+---------------------------------------------------------------+
| Ctrl+Y       | Redoes the last operation.                                    |
+--------------+---------------------------------------------------------------+
| Left         | Moves the cursor one character to the left.                   |
+--------------+---------------------------------------------------------------+
| Ctrl+Left    | Moves the cursor one word to the left.                        |
+--------------+---------------------------------------------------------------+
| Right        | Moves the cursor one character to the right.                  |
+--------------+---------------------------------------------------------------+
| Ctrl+Right   | Moves the cursor one word to the right.                       |
+--------------+---------------------------------------------------------------+
| Up           | Moves the cursor one line up.                                 |
+--------------+---------------------------------------------------------------+
| Down         | Moves the cursor one line down.                               |
+--------------+---------------------------------------------------------------+
| PageUp       | Moves the cursor one page up.                                 |
+--------------+---------------------------------------------------------------+
| PageDown     | Moves the cursor one page down.                               |
+--------------+---------------------------------------------------------------+
| Home         | Moves the cursor to the beginning of the line.                |
+--------------+---------------------------------------------------------------+
| Ctrl+Home    | Moves the cursor to the beginning of the text.                |
+--------------+---------------------------------------------------------------+
| End          | Moves the cursor to the end of the line.                      |
+--------------+---------------------------------------------------------------+
| Ctrl+End     | Moves the cursor to the end of the text.                      |
+--------------+---------------------------------------------------------------+
| Alt+Wheel    | Scrolls the page horizontally (the Wheel is the mouse wheel). |
+--------------+---------------------------------------------------------------+

To select (mark) text hold down the Shift key whilst pressing one of the movement keystrokes, for example, *Shift+Right* will select the character to the right, and *Shift+Ctrl+Right* will select the word to the right, etc.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument`, :sip:ref:`~PyQt6.QtGui.QTextCursor`, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_, `Syntax Highlighter Example <https://doc.qt.io/qt-6/qtwidgets-richtext-syntaxhighlighter-example.html>`_, `Rich Text Processing <https://doc.qt.io/qt-6/richtext.html>`_.

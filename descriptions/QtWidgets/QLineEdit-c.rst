.. sip:class-description::
    :status: todo
    :brief: One-line text editor
    :digest: a03a18bc1394afce1324f40845aa6214

The :sip:ref:`~PyQt6.QtWidgets.QLineEdit` widget is a one-line text editor.

.. image:: ../../../images/windows-lineedit.png

A line edit allows users to enter and edit a single line of plain text with useful editing functions, including undo and redo, cut and paste, and drag and drop.

By changing the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.echoMode` of a line edit, it can also be used as a write-only field for inputs such as passwords.

:sip:ref:`~PyQt6.QtWidgets.QTextEdit` is a related class that allows multi-line, rich text editing.

.. _qlineedit-constraining-text:

Constraining Text
-----------------

Use :sip:ref:`~PyQt6.QtWidgets.QLineEdit.maxLength` to define the maximum permitted length of a text. You can use a :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setValidator` to further constrain the text content.

.. _qlineedit-editing-text:

Editing Text
------------

You can change the text with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.insert`. Use :sip:ref:`~PyQt6.QtWidgets.QLineEdit.text` to retrieve the text and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.displayText` to retrieve the displayed text (which may be different, see :sip:ref:`~PyQt6.QtWidgets.QLineEdit.EchoMode.EchoMode`). You can select the text with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setSelection` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.selectAll`, and you can :sip:ref:`~PyQt6.QtWidgets.QLineEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.copy`, and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.paste` the selection. To align the text, use :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setAlignment`.

When the text changes, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textChanged` signal is emitted. When the text changes in some other way than by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText`, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textEdited` signal is emitted. When the cursor is moved, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.cursorPositionChanged` signal is emitted. And when the Return or Enter key is selected, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed` signal is emitted.

When text editing is finished, either because the line edit lost focus or Return/Enter was selected, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signal is emitted.

If the line edit focus is lost without any text changes, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signal won't be emitted.

If there is a validator set on the line edit, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed`/\ :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signals will only be emitted if the validator returns :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`.

For more information on the many ways that :sip:ref:`~PyQt6.QtWidgets.QLineEdit` can be used, see `Line Edits Example <https://doc.qt.io/qt-6/qtwidgets-widgets-lineedits-example.html>`_, which also provides a selection of line edit examples that show the effects of various properties and validators on the input and output supplied by the user.

.. _qlineedit-setting-a-frame:

Setting a Frame
---------------

By default, QLineEdits have a frame as specified in the platform style guides. You can turn the frame off by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setFrame`\ (false).

.. _qlineedit-default-key-bindings:

Default Key Bindings
--------------------

The table below describes the default key bindings.

**Note:** The line edit also provides a context menu (usually invoked by a right-click) that presents some of the editing options listed below.

.. _qlineedit-desc:

+-------------------+-----------------------------------------------------------+
| Keystroke         | Action                                                    |
+===================+===========================================================+
| Left Arrow        | Moves the cursor one character to the left.               |
+-------------------+-----------------------------------------------------------+
| Shift+Left Arrow  | Moves and selects text one character to the left.         |
+-------------------+-----------------------------------------------------------+
| Right Arrow       | Moves the cursor one character to the right.              |
+-------------------+-----------------------------------------------------------+
| Shift+Right Arrow | Moves and selects text one character to the right.        |
+-------------------+-----------------------------------------------------------+
| Home              | Moves the cursor to the beginning of the line.            |
+-------------------+-----------------------------------------------------------+
| End               | Moves the cursor to the end of the line.                  |
+-------------------+-----------------------------------------------------------+
| Backspace         | Deletes the character to the left of the cursor.          |
+-------------------+-----------------------------------------------------------+
| Ctrl+Backspace    | Deletes the word to the left of the cursor.               |
+-------------------+-----------------------------------------------------------+
| Delete            | Deletes the character to the right of the cursor.         |
+-------------------+-----------------------------------------------------------+
| Ctrl+Delete       | Deletes the word to the right of the cursor.              |
+-------------------+-----------------------------------------------------------+
| Ctrl+A            | Selects all.                                              |
+-------------------+-----------------------------------------------------------+
| Ctrl+C            | Copies the selected text to the clipboard.                |
+-------------------+-----------------------------------------------------------+
| Ctrl+Insert       | Copies the selected text to the clipboard.                |
+-------------------+-----------------------------------------------------------+
| Ctrl+K            | Deletes to the end of the line.                           |
+-------------------+-----------------------------------------------------------+
| Ctrl+V            | Pastes the clipboard text into line edit.                 |
+-------------------+-----------------------------------------------------------+
| Shift+Insert      | Pastes the clipboard text into line edit.                 |
+-------------------+-----------------------------------------------------------+
| Ctrl+X            | Deletes the selected text and copies it to the clipboard. |
+-------------------+-----------------------------------------------------------+
| Shift+Delete      | Deletes the selected text and copies it to the clipboard. |
+-------------------+-----------------------------------------------------------+
| Ctrl+Z            | Undoes the last operation.                                |
+-------------------+-----------------------------------------------------------+
| Ctrl+Y            | Redoes the last undone operation.                         |
+-------------------+-----------------------------------------------------------+

Any other keystroke that represents a valid character, will cause the character to be inserted into the line edit.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtWidgets.QLabel`, :sip:ref:`~PyQt6.QtWidgets.QComboBox`, `Line Edits Example <https://doc.qt.io/qt-6/qtwidgets-widgets-lineedits-example.html>`_.

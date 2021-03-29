.. sip:class-description::
    :status: todo
    :brief: One-line text editor
    :digest: a36e6bdc3ef97e23dba57d212f5f3eb6

The :sip:ref:`~PyQt6.QtWidgets.QLineEdit` widget is a one-line text editor.

.. image:: ../../../images/windows-lineedit.png

A line edit allows the user to enter and edit a single line of plain text with a useful collection of editing functions, including undo and redo, cut and paste, and drag and drop (see :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setDragEnabled`).

By changing the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.echoMode` of a line edit, it can also be used as a "write-only" field, for inputs such as passwords.

The length of the text can be constrained to :sip:ref:`~PyQt6.QtWidgets.QLineEdit.maxLength`. The text can be arbitrarily constrained using a :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` or an :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask`, or both. When switching between a validator and an input mask on the same line edit, it is best to clear the validator or input mask to prevent undefined behavior.

A related class is :sip:ref:`~PyQt6.QtWidgets.QTextEdit` which allows multi-line, rich text editing.

You can change the text with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.insert`. The text is retrieved with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.text`; the displayed text (which may be different, see :sip:ref:`~PyQt6.QtWidgets.QLineEdit.EchoMode.EchoMode`) is retrieved with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.displayText`. Text can be selected with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setSelection` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.selectAll`, and the selection can be :sip:ref:`~PyQt6.QtWidgets.QLineEdit.cut`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.copy`\ ied and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.paste`\ d. The text can be aligned with :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setAlignment`.

When the text changes the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textChanged` signal is emitted; when the text changes other than by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText` the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textEdited` signal is emitted; when the cursor is moved the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.cursorPositionChanged` signal is emitted; and when the Return or Enter key is pressed the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed` signal is emitted.

When editing is finished, either because the line edit lost focus or Return/Enter is pressed the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signal is emitted.

Note that if there is a validator set on the line edit, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed`/\ :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signals will only be emitted if the validator returns :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`.

By default, QLineEdits have a frame as specified by platform style guides; you can turn it off by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setFrame`\ (false).

The default key bindings are described below. The line edit also provides a context menu (usually invoked by a right mouse click) that presents some of these editing options.

.. _qlineedit-desc:

+-------------------+-----------------------------------------------------------+
| Keypress          | Action                                                    |
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
| Ctrl+A            | Select all.                                               |
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

Any other key sequence that represents a valid character, will cause the character to be inserted into the line edit.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtWidgets.QLabel`, `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_, `GUI Design Handbook: Field, Entry <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Line Edits Example <https://doc.qt.io/qt-6/qtwidgets-widgets-lineedits-example.html>`_.

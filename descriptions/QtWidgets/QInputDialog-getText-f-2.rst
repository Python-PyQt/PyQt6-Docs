.. sip:method-description::
    :status: todo
    :pysig: a15cdae0d226023e28c53ba044c88191
    :realsig: (QWidget*, const QString&, const QString&, QLineEdit::EchoMode, const QString&, bool*, Qt::WindowFlags, Qt::InputMethodHints)
    :digest: f3fcd8312132883766df0b72baabb158

Static convenience function to get a string from the user.

*title* is the text which is displayed in the title bar of the dialog. *label* is the text which is shown to the user (it should say what should be entered). *text* is the default text which is placed in the line edit. *mode* is the echo mode the line edit will use. *inputMethodHints* is the input method hints that will be used in the edit widget if an input method is active.

If *ok* is nonnull *\*ok* will be set to true if the user pressed OK and to false if the user pressed Cancel. The dialog's parent is *parent*. The dialog will be modal and uses the specified widget *flags*.

If the dialog is accepted, this function returns the text in the dialog's line edit. If the dialog is rejected, a null QString is returned.

Use this static function like this:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 358-363

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getInt`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getDouble`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getItem`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getMultiLineText`.

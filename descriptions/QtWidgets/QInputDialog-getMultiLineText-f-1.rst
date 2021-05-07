.. sip:method-description::
    :status: todo
    :pysig: 8fa381f64dfb0d1f393c7f729de877c7
    :realsig: (QWidget*,const QString&,const QString&,const QString&,bool*,Qt::WindowFlags,Qt::InputMethodHints)
    :digest: 55721a52f8d21de5c841fac340cea1dd

Static convenience function to get a multiline string from the user.

*title* is the text which is displayed in the title bar of the dialog. *label* is the text which is shown to the user (it should say what should be entered). *text* is the default text which is placed in the plain text edit. *inputMethodHints* is the input method hints that will be used in the edit widget if an input method is active.

If *ok* is nonnull *\*ok* will be set to true if the user pressed OK and to false if the user pressed Cancel. The dialog's parent is *parent*. The dialog will be modal and uses the specified widget *flags*.

If the dialog is accepted, this function returns the text in the dialog's plain text edit. If the dialog is rejected, a null QString is returned.

Use this static function like this:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 370-374

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getInt`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getDouble`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getItem`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`.

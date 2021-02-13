.. sip:method-description::
    :status: todo
    :pysig: c9eb113059e11fb0719f5e011949c93c
    :realsig: (QWidget*,const QString&,const QString&,const QStringList&,int,bool,bool*,Qt::WindowFlags,Qt::InputMethodHints)
    :digest: c5d394c1aeee2e2581fc576d720ef32d

Static convenience function to let the user select an item from a string list.

*title* is the text which is displayed in the title bar of the dialog. *label* is the text which is shown to the user (it should say what should be entered). *items* is the string list which is inserted into the combo box. *current* is the number of the item which should be the current item. *inputMethodHints* is the input method hints that will be used if the combo box is editable and an input method is active.

If *editable* is true the user can enter their own text; otherwise, the user may only select one of the existing items.

If *ok* is nonnull *\*ok* will be set to true if the user pressed OK and to false if the user pressed Cancel. The dialog's parent is *parent*. The dialog will be modal and uses the widget *flags*.

This function returns the text of the current item, or if *editable* is true, the current text of the combo box.

Use this static function like this:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 344-351

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getInt`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getDouble`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getMultiLineText`.

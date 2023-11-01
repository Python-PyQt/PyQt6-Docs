.. sip:method-description::
    :status: todo
    :pysig: 66240179f4d923cfd4a9097e49b8b32f
    :realsig: (QWidget*, const QString&, const QString&, int, int, int, int, bool*, Qt::WindowFlags)
    :digest: fe1a7ce419e1ffaf048b5c3df57668f4

Static convenience function to get an integer input from the user.

*title* is the text which is displayed in the title bar of the dialog. *label* is the text which is shown to the user (it should say what should be entered). *value* is the default integer which the spinbox will be set to. *min* and *max* are the minimum and maximum values the user may choose. *step* is the amount by which the values change as the user presses the arrow buttons to increment or decrement the value.

If *ok* is nonnull \*\ *ok* will be set to true if the user pressed OK and to false if the user pressed Cancel. The dialog's parent is *parent*. The dialog will be modal and uses the widget *flags*.

On success, this function returns the integer which has been entered by the user; on failure, it returns the initial *value*.

Use this static function like this:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 321-325

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getDouble`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getItem`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getMultiLineText`.

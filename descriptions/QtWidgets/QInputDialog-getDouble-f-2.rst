.. sip:method-description::
    :status: todo
    :pysig: f8c3d2da23df0a78402ddf937b470f96
    :realsig: (QWidget*, const QString&, const QString&, double, double, double, int, bool*, Qt::WindowFlags, double)
    :digest: c8ba0879dca539e7bbcf0cedea18c728

Static convenience function to get a floating point number from the user.

*title* is the text which is displayed in the title bar of the dialog. *label* is the text which is shown to the user (it should say what should be entered). *value* is the default floating point number that the line edit will be set to. *min* and *max* are the minimum and maximum values the user may choose. *decimals* is the maximum number of decimal places the number may have. *step* is the amount by which the values change as the user presses the arrow buttons to increment or decrement the value.

If *ok* is nonnull, \*\ *ok* will be set to true if the user pressed OK and to false if the user pressed Cancel. The dialog's parent is *parent*. The dialog will be modal and uses the widget *flags*.

This function returns the floating point number which has been entered by the user.

Use this static function like this:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 332-337

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getInt`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getItem`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getMultiLineText`.

.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: a8169789687952af0c19857889c36fe9

This signal is emitted whenever a checkable button changes its state. *checked* is true if the button is checked, or false if the button is unchecked.

This may be the result of a user action, :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.click` slot activation, or because :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setChecked` is called.

The states of buttons in exclusive button groups are updated before this signal is emitted. This means that slots can act on either the "off" signal or the "on" signal emitted by the buttons in the group whose states have changed.

For example, a slot that reacts to signals emitted by newly checked buttons but which ignores signals from buttons that have been unchecked can be implemented using the following pattern:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qabstractbutton.py
    :lines: 65-71

Button groups can be created using the :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` class, and updates to the button states monitored with the :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.buttonClicked` signal.

.. seealso:: checked, :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.clicked`.

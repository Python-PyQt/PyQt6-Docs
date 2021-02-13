.. sip:method-description::
    :status: todo
    :pysig: 269f244f12edb760aa12edd873c6e9eb
    :realsig: (QLineEdit*)
    :digest: 86b6376a02eb7ac45b48c24df82a6c4d

Sets the line *edit* to use instead of the current line edit widget.

The combo box takes ownership of the line edit.

**Note:** Since the combobox's line edit owns the :sip:ref:`~PyQt6.QtWidgets.QCompleter`, any previous call to :sip:ref:`~PyQt6.QtWidgets.QComboBox.setCompleter` will no longer have any effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.lineEdit`.

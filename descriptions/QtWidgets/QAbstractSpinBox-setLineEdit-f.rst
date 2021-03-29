.. sip:method-description::
    :status: todo
    :pysig: 269f244f12edb760aa12edd873c6e9eb
    :realsig: (QLineEdit*)
    :digest: f8725a63080830ea57bba3d7d9c1ee10

Sets the line edit of the spinbox to be *lineEdit* instead of the current line edit widget. *lineEdit* cannot be ``nullptr``.

:sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` takes ownership of the new :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.lineEdit`

If :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` for the *lineEdit* returns ``nullptr``, the internal validator of the spinbox will be set on the line edit.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.lineEdit`.

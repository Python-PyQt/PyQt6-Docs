.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ca2376aeb804e47fecda2a24d77e4a40

This signal is emitted when the Return or Enter key is used, or if the line edit loses focus and its contents have changed since the last time this signal was emitted.

**Note:** If there is a :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` set on the line edit and enter/return is used, the editingFinished() signal will only be emitted if the input follows the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` and the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` returns :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`.

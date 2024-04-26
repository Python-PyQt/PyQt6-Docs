.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 07038676b16ab52607e057036de69220

This signal is emitted when the Return or Enter key is used.

**Note:** If there is a :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` set on the line edit, the returnPressed() signal will only be emitted if the input follows the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` and the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` returns :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`.

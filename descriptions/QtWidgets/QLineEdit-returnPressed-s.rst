.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7c18d3243a1a1f729c00884a6903d6d8

This signal is emitted when the Return or Enter key is pressed. Note that if there is a :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` set on the line edit, the  signal will only be emitted if the input follows the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask` and the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator` returns :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`.

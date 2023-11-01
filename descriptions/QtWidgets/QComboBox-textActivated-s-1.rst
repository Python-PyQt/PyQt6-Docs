.. sip:signal-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 4d3d06db032969183d8374f2355434fd

This signal is sent when the user chooses an item in the combobox. The item's *text* is passed. Note that this signal is sent even when the choice is not changed. If you need to know when the choice actually changes, use signal :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndexChanged` or :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentTextChanged`.

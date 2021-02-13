.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 51e331b066ba734a7878443242eef254

This signal is sent when the user chooses an item in the combobox. The item's *index* is passed. Note that this signal is sent even when the choice is not changed. If you need to know when the choice actually changes, use signal :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndexChanged` or :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentTextChanged`.

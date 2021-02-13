.. sip:signal-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 4e1ed626c8b359ae66937270698f76ec

This signal is emitted whenever the text changes. The *text* argument is the new text.

Unlike :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textEdited`, this signal is also emitted when the text is changed programmatically, for example, by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText`.

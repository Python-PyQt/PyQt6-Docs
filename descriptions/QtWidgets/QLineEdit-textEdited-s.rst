.. sip:signal-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: d64a6b2596b4bcd28c0a07d1ccd604e9

This signal is emitted whenever the text is edited. The *text* argument is the new text.

Unlike :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textChanged`, this signal is not emitted when the text is changed programmatically, for example, by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText`.

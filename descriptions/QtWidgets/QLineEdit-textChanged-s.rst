.. sip:signal-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 4e1ed626c8b359ae66937270698f76ec

This signal is emitted whenever the text changes. The *text* argument is the new text.

Unlike :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textEdited`, this signal is also emitted when the text is changed programmatically, for example, by calling :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setText`.

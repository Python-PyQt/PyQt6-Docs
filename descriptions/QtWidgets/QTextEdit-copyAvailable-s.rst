.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 277a562f496bf0be47386256bf66d3fe

This signal is emitted when text is selected or de-selected in the text edit.

When text is selected this signal will be emitted with *yes* set to true. If no text has been selected or if the selected text is de-selected this signal is emitted with *yes* set to false.

If *yes* is true then :sip:ref:`~PyQt6.QtWidgets.QTextEdit.copy` can be used to copy the selection to the clipboard. If *yes* is false then :sip:ref:`~PyQt6.QtWidgets.QTextEdit.copy` does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit.selectionChanged`.

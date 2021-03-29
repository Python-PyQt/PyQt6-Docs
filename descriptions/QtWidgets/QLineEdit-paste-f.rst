.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ac0768d6fa40efd1f1680c2177475f1d

Inserts the clipboard's text at the cursor position, deleting any selected text, providing the line edit is not read-only.

If the end result would be invalid to the current :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setValidator`, nothing happens.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit.copy`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.cut`.

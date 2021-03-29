.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 9e49a45c4fb836892b57cb5462565c69

Deletes row *row* from this form layout.

*row* must be non-negative and less than :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount`.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 91-95

If you want to remove the row from the layout without deleting the widgets, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow`.

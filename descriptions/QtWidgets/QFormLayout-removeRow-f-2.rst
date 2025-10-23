.. sip:method-description::
    :status: todo
    :pysig: 2f0da4d3658dfe115217ca868dfa5e64
    :realsig: (QLayout*)
    :digest: b476ea08809b84114e1dc123f2b7dd73

Deletes the row corresponding to *layout* from this form layout.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 107-111

If you want to remove the row from the form layout without deleting the inserted layout, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow`.

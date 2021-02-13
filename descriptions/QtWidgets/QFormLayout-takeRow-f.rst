.. sip:method-description::
    :status: todo
    :pysig: fc51a02303e6eba5856b14463d90afd3
    :realsig: (int)
    :digest: a91d208eff2265ec820024ff0616761c

Removes the specified *row* from this form layout.

*row* must be non-negative and less than :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount`.

**Note:** This function doesn't delete anything.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 115-119

If you want to remove the row from the layout and delete the widgets, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow` instead.

Returns A structure containing both the widget and corresponding label layout items

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow`.

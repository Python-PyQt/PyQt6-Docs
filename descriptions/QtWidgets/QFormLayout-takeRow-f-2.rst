.. sip:method-description::
    :status: todo
    :pysig: 9625ed420a648efd68e768922e6b8dd7
    :realsig: (QLayout*)
    :digest: a3a2649015d02051f38245351a161924

Removes the specified *layout* from this form layout.

**Note:** This function doesn't delete anything.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 131-135

If you want to remove the row from the form layout and delete the inserted layout, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow` instead.

Returns A structure containing both the widget and corresponding label layout items

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow`.

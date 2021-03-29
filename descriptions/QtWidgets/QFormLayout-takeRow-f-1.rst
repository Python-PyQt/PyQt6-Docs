.. sip:method-description::
    :status: todo
    :pysig: d41c3808f0c7c2dcd2abb131f18044db
    :realsig: (QWidget*)
    :digest: 757ec6f3770ec93f8f13c40b38c78441

This is an overloaded function.

Removes the specified *widget* from this form layout.

**Note:** This function doesn't delete anything.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 123-127

If you want to remove the row from the layout and delete the widgets, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow` instead.

Returns A structure containing both the widget and corresponding label layout items

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.removeRow`.

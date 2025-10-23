.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 3b933cc7fb5c1f3c147b90670b61677d

Deletes the row corresponding to *widget* from this form layout.

After this call, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.rowCount` is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 99-103

If you want to remove the row from the layout without deleting the widgets, use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.takeRow`.

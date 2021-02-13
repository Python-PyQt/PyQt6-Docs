.. sip:method-description::
    :status: todo
    :pysig: d3cf020e4b0aa89c323f52c8f0ab0379
    :realsig: (int,QFormLayout::ItemRole,QWidget*)
    :digest: 344b4ebcd5695e32648a78d6b820ec56

Sets the widget in the given *row* for the given *role* to *widget*, extending the layout with empty rows if necessary.

If the cell is already occupied, the *widget* is not inserted and an error message is sent to the console.

**Note:** For most applications, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow` should be used instead of .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setLayout`.

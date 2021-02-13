.. sip:method-description::
    :status: todo
    :pysig: b0ef72e44dfe4c746194629be7868823
    :realsig: (int,QFormLayout::ItemRole,QLayout*)
    :digest: c44fc723b67bddaeeab797cd172e2b4d

Sets the sub-layout in the given *row* for the given *role* to *layout*, extending the form layout with empty rows if necessary.

If the cell is already occupied, the *layout* is not inserted and an error message is sent to the console.

**Note:** For most applications, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.insertRow` should be used instead of .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setWidget`.

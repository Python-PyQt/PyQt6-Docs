.. sip:method-description::
    :status: todo
    :pysig: a4602086a32960a08a50bffcc1b15247
    :realsig: (int,QFormLayout::ItemRole,QLayoutItem*)
    :digest: 4f97ef5395442e4688c1c4f58060c213

Sets the item in the given *row* for the given *role* to *item*, extending the layout with empty rows if necessary.

If the cell is already occupied, the *item* is not inserted and an error message is sent to the console. The *item* spans both columns.

**Warning:** Do not use this function to add child layouts or child widget items. Use :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setLayout` or :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setWidget` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setLayout`.

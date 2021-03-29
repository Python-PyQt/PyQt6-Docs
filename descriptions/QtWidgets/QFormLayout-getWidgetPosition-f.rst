.. sip:method-description::
    :status: todo
    :pysig: 5c847f7699c101c4de3755455f3080af
    :realsig: (QWidget*,int*,QFormLayout::ItemRole*) const
    :digest: 713f3db53558daa8d6db55bd923f548f

Retrieves the row and role (column) of the specified *widget* in the layout. If *widget* is not in the layout, \*\ *rowPtr* is set to -1; otherwise the row is stored in \*\ *rowPtr* and the role is stored in \*\ *rolePtr*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.getItemPosition`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.itemAt`.

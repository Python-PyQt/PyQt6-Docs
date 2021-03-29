.. sip:method-description::
    :status: todo
    :pysig: 3c556d694a317c51af5b223ee97e3b96
    :realsig: (int,int*,QFormLayout::ItemRole*) const
    :digest: acb80482d5dc8556358cb67084fd1025

Retrieves the row and role (column) of the item at the specified *index*. If *index* is out of bounds, \*\ *rowPtr* is set to -1; otherwise the row is stored in \*\ *rowPtr* and the role is stored in \*\ *rolePtr*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFormLayout.itemAt`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.count`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.getLayoutPosition`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.getWidgetPosition`.

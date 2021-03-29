.. sip:method-description::
    :status: todo
    :pysig: dda4d4157806d9fb40b7394b87b3266a
    :realsig: () const
    :digest: efb7566ffde4f70f50da96220edcdb5a

Returns a copy of this item. The item's children are not copied.

When subclassing :sip:ref:`~PyQt6.QtGui.QStandardItem`, you can reimplement this function to provide :sip:ref:`~PyQt6.QtGui.QStandardItemModel` with a factory that it can use to create new items on demand.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setItemPrototype`, operator=().

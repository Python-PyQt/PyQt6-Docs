.. sip:method-description::
    :status: todo
    :pysig: dda4d4157806d9fb40b7394b87b3266a
    :realsig: (const QStandardItem*)
    :digest: 1627d1a9df5375e17bfb74d571a4626f

Sets the item prototype for the model to the specified *item*. The model takes ownership of the prototype.

The item prototype acts as a :sip:ref:`~PyQt6.QtGui.QStandardItem` factory, by relying on the :sip:ref:`~PyQt6.QtGui.QStandardItem.clone` function. To provide your own prototype, subclass :sip:ref:`~PyQt6.QtGui.QStandardItem`, reimplement :sip:ref:`~PyQt6.QtGui.QStandardItem.clone` and set the prototype to be an instance of your custom class. Whenever :sip:ref:`~PyQt6.QtGui.QStandardItemModel` needs to create an item on demand (for instance, when a view or item delegate calls :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setData`)), the new items will be instances of your custom class.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemPrototype`, :sip:ref:`~PyQt6.QtGui.QStandardItem.clone`.

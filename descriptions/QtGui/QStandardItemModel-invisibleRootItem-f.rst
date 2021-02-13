.. sip:method-description::
    :status: todo
    :pysig: dda4d4157806d9fb40b7394b87b3266a
    :realsig: () const
    :digest: c57d3d10331d62a66241ad1eddecddc4

Returns the model's invisible root item.

The invisible root item provides access to the model's top-level items through the :sip:ref:`~PyQt6.QtGui.QStandardItem` API, making it possible to write functions that can treat top-level items and their children in a uniform way; for example, recursive functions involving a tree model.

**Note:** Calling :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.index` on the :sip:ref:`~PyQt6.QtGui.QStandardItem` object retrieved from this function is not valid.

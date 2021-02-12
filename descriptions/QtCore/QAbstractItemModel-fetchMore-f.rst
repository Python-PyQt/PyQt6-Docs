.. sip:method-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: (const QModelIndex&)
    :digest: d740d5093ac83ca42a52711a0193747b

Fetches any available data for the items with the parent specified by the *parent* index.

Reimplement this if you are populating your model incrementally.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.canFetchMore`.

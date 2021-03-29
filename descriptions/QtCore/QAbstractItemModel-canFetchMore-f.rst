.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&) const
    :digest: 6e990c1e818a5b438fb743daf9f91f34

Returns ``true`` if there is more data available for *parent*; otherwise returns ``false``.

The default implementation always returns ``false``.

If  returns ``true``, the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` function should be called. This is the behavior of :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore`.

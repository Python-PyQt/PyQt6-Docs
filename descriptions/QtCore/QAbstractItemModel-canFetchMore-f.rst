.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&) const
    :digest: 092be28c315bb84703c11036d045a9bb

Returns ``true`` if there is more data available for *parent*; otherwise returns ``false``.

The default implementation always returns ``false``.

If canFetchMore() returns ``true``, the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` function should be called. This is the behavior of :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore`.

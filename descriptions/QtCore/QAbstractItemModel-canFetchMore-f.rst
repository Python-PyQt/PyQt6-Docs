.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&) const
    :digest: ecaeb3812ea6ee17d6f183915f554d64

Returns ``true`` if there is more data available for *parent*; otherwise returns ``false``.

The default implementation always returns ``false``.

If  returns ``true``, the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` function should be called. This is the behavior of QAbstractItemView, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore`.

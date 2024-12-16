.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 5f255588014cb3d91f1b866cefb846b8

If *b* is ``true``, this proxy model will handle the source model layout changes (by connecting to ``QAbstractItemModel::layoutAboutToBeChanged`` and ``QAbstractItemModel::layoutChanged`` signals).

The default is for this proxy model to handle the source model layout changes.

In sub-classes of :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel`, it may be useful to set this to ``false`` if you need to specially handle the source model layout changes.

**Note:** Calling this method will only have an effect after calling :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel.setSourceModel`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel.handleSourceLayoutChanges`.

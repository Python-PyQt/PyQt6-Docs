.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 535467163c6b5d3f8aa90e5e19985741

If *b* is ``true``, this proxy model will handle the source model data changes (by connecting to ``QAbstractItemModel::dataChanged`` signal).

The default is for this proxy model to handle the source model data changes.

In sub-classes of :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel`, it may be useful to set this to ``false`` if you need to specially handle the source model data changes.

**Note:** Calling this method will only have an effect after calling :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel.setSourceModel`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel.handleSourceDataChanges`.

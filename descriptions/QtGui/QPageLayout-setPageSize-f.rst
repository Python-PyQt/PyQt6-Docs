.. sip:method-description::
    :status: todo
    :pysig: b1091dbc8c68d217e9d0a4dc317fc96f
    :realsig: (const QPageSize&,const QMarginsF&)
    :digest: 8ddea127623a6781cfd09759a9c82920

Sets the page size of the page layout to *pageSize*.

Optionally define the minimum allowed margins *minMargins*, e.g. the minimum margins able to be printed by a physical print device, otherwise the minimum margins will default to 0.

If :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode` is set then the existing margins will be clamped to the new minimum margins and the maximum margins allowed by the page size. If :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` is set then the existing margins will be unchanged.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.pageSize`.

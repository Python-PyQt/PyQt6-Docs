.. sip:method-description::
    :status: todo
    :pysig: 832c1ef14febe868731feb4b28a7c982
    :realsig: (const QPageSize&,QPageLayout::Orientation,const QMarginsF&,QPageLayout::Unit,const QMarginsF&)
    :digest: 4524a27deca0882aeafe217ea12e9f6f

Creates a :sip:ref:`~PyQt6.QtGui.QPageLayout` with the given *pageSize*, *orientation* and *margins* in the given *units*.

Optionally define the minimum allowed margins *minMargins*, e.g. the minimum margins able to be printed by a physical print device.

The constructed :sip:ref:`~PyQt6.QtGui.QPageLayout` will be in :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode`.

The *margins* given will be clamped to the minimum margins and the maximum margins allowed by the page size.

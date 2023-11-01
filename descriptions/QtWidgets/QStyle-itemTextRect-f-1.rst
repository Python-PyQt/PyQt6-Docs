.. sip:method-description::
    :status: todo
    :pysig: 85b75dd031da6be78a7b8dbdb3d46cc5
    :realsig: (const QFontMetrics&, const QRect&, int, bool, const QString&) const
    :digest: 000db4c839d103a180443a2b7967cf5e

Returns the area within the given *rectangle* in which to draw the provided *text* according to the specified font *metrics* and *alignment*. The *enabled* parameter indicates whether or not the associated item is enabled.

If the given *rectangle* is larger than the area needed to render the *text*, the rectangle that is returned will be offset within *rectangle* according to the specified *alignment*. For example, if *alignment* is :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignCenter`, the returned rectangle will be centered within *rectangle*. If the given *rectangle* is smaller than the area needed, the returned rectangle will be the smallest rectangle large enough to render the *text*.

.. seealso:: Qt::Alignment.

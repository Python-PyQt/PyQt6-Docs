.. sip:method-description::
    :status: todo
    :pysig: 9b844015e1302619c8f96ba59db1d3aa
    :realsig: (const QRect&) const
    :digest: 77e68d5d010a5be774f6cae2a6eb1d80

Returns the intersection of this rectangle and the given *rectangle*. Note that ``r.intersected(s)`` is equivalent to ``r & s``.

.. image:: ../../../images/qrect-intersect.png

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.intersects`, :sip:ref:`~PyQt6.QtCore.QRect.united`, operator&=().

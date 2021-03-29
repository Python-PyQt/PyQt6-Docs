.. sip:method-description::
    :status: todo
    :pysig: 10b73e32ef579338968290bf7f39b35c
    :realsig: (const QRectF&) const
    :digest: 77e68d5d010a5be774f6cae2a6eb1d80

Returns the intersection of this rectangle and the given *rectangle*. Note that ``r.intersected(s)`` is equivalent to ``r & s``.

.. image:: ../../../images/qrect-intersect.png

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRectF.intersects`, :sip:ref:`~PyQt6.QtCore.QRectF.united`, operator&=().

.. sip:method-description::
    :status: todo
    :pysig: cc9071d3b59a402ce38a20e0550b379b
    :realsig: (const QRegion&) const
    :digest: e2aba63b366949a73f63220c83f63763

Returns a region which is *r* subtracted from this region.

.. image:: ../../../images/rsubtract.png

The figure shows the result when the ellipse on the right is subtracted from the ellipse on the left (``left - right``).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QRegion.intersected`, :sip:ref:`~PyQt6.QtGui.QRegion.united`, :sip:ref:`~PyQt6.QtGui.QRegion.xored`.

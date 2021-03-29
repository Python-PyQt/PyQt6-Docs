.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: e56a011360bba9acc8e8fb3d7dcf751b

Returns the normalized position of this point.

The coordinates are calculated by transforming :sip:ref:`~PyQt6.QtGui.QEventPoint.globalPosition` into the space of :sip:ref:`~PyQt6.QtGui.QInputDevice.availableVirtualGeometry`, i.e. ``(0, 0)`` is the top-left corner and ``(1, 1)`` is the bottom-right corner.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QEventPoint.globalPosition`.

.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: 8bb0589f4e4f138c7fc9258ec947890f

Returns the offset of the dirty regions in the view.

If you use :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.scrollDirtyRegion` and implement a paintEvent() in a subclass of :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, you should translate the area given by the paint event with the offset returned from this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.scrollDirtyRegion`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setDirtyRegion`.

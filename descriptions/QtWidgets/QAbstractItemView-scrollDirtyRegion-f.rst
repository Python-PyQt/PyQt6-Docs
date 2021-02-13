.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: d5803de51d58a7f0fad5558914ac2974

Prepares the view for scrolling by (\ *dx*,\ *dy*) pixels by moving the dirty regions in the opposite direction. You only need to call this function if you are implementing a scrolling viewport in your view subclass.

If you implement scrollContentsBy() in a subclass of :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, call this function before you call :sip:ref:`~PyQt6.QtWidgets.QWidget.scroll` on the viewport. Alternatively, just call :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.update`.

.. seealso:: scrollContentsBy(), :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.dirtyRegionOffset`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setDirtyRegion`.

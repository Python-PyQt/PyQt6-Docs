.. sip:method-description::
    :status: todo
    :pysig: 310cd3e0a237f2222b759579115b6cdc
    :realsig: (int) const
    :digest: 89b3d85ab0e1ca3da29d9eb3d0dc058f

Returns the timeline value for the time *msec*. The returned value, which varies depending on the curve shape, is always between 0 and 1. If *msec* is 0, the default implementation always returns 0.

Reimplement this function to provide a custom curve shape for your timeline.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.easingCurve`, :sip:ref:`~PyQt6.QtCore.QTimeLine.frameForTime`.

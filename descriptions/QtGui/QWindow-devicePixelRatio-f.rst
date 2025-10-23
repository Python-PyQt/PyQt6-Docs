.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: a516f554f258e89158cc0077b6ca28b3

Returns the ratio between physical pixels and device-independent pixels for the window. This value is dependent on the screen the window is on, and may change when the window is moved.

The :sip:ref:`~PyQt6.QtGui.QWindow` instance receives an event of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.DevicePixelRatioChange` when the device pixel ratio changes.

Common values are 1.0 on normal displays and 2.0 on Apple "retina" displays.

**Note:** For windows not backed by a platform window, meaning that :sip:ref:`~PyQt6.QtGui.QWindow.create` was not called, the function will fall back to the associated :sip:ref:`~PyQt6.QtGui.QScreen`'s device pixel ratio.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QScreen.devicePixelRatio`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.DevicePixelRatioChange`.

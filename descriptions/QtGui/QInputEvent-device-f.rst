.. sip:method-description::
    :status: todo
    :pysig: 48c517bd5e69c86713c2fa60214c992e
    :realsig: () const
    :digest: 89e6c4ef07ee8f6308ee2bec4ebca3f4

Returns the source device that generated the original event.

In case of a synthesized event, for example a mouse event that was generated from a touch event, ``device()`` continues to return the touchscreen device, so that you can tell that it did not come from an actual mouse. Thus ``mouseEvent.source()->type() != QInputDevice::DeviceType::Mouse`` is one possible replacement for the Qt 5 expression ``mouseEvent.source() == Qt::MouseEventSynthesizedByQt``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPointerEvent.pointingDevice`.

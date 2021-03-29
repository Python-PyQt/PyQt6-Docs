.. sip:class-description::
    :status: todo
    :brief: Identifies a unique object, such as a tagged token or stylus, which is used with a pointing device
    :digest: cabcfba740d6d496dd3c5182164f711b

:sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId` identifies a unique object, such as a tagged token or stylus, which is used with a pointing device.

QPointingDeviceUniqueIds can be compared for equality, and can be used as keys in a QHash. You get access to the numerical ID via :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId.numericId`, if the device supports such IDs. For future extensions, though, you should not use that function, but compare objects of this type using the equality operator.

This class is a thin wrapper around an integer ID. You pass it into and out of functions by value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QEventPoint`.

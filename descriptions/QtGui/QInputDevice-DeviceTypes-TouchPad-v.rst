.. sip:enum-member-description::
    :status: todo
    :value: 0x0004
    :realname: QInputDevice::DeviceType::TouchPad
    :digest: fd7555fcb3c6ed4980c8cd0258c6676f

In this type of device, the touch surface is separate from the display. There is not a direct relationship between the physical touch location and the on-screen coordinates. Instead, they are calculated relative to the current mouse position, and the user must use the touch-pad to move this reference point. Unlike touch-screens, Qt allows users to only interact with a single QWidget or QGraphicsItem at a time.

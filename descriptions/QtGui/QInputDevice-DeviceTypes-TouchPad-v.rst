.. sip:enum-member-description::
    :status: todo
    :value: 0x0004
    :realname: QInputDevice::DeviceType::TouchPad
    :digest: 584ba45654970f44c9e396aaed0ba14d

In this type of device, the touch surface is separate from the display. There is not a direct relationship between the physical touch location and the on-screen coordinates. Instead, they are calculated relative to the current mouse position, and the user must use the touch-pad to move this reference point. Unlike touch-screens, Qt allows users to only interact with a single `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` at a time.

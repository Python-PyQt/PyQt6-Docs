.. sip:method-description::
    :status: todo
    :pysig: 6b492fe03e436348e2b711199f5a627a
    :realsig: (const QString&,qint64,QInputDevice::DeviceType,const QString&,QObject*)
    :digest: c49ebe6201de5131e2816bae860ea202

Creates a new input device instance. The given *name* is normally a manufacturer-assigned model name if available, or something else identifiable; *id* is a platform-specific number that will be unique per device (for example the xinput ID on X11); *type* identifies what kind of device. On window systems that are capable of handling input from multiple users or sets of input devices at the same time (such as Wayland or X11), *seatName* identifies the name of the set of devices that will be used together. If the device is a child or slave device (for example one of several mice that can take turns moving the "core pointer"), the master device should be given as the *parent*.

The platform plugin creates, registers and continues to own each device instance; usually *parent* should be given for memory management purposes even if there is no master for a particular device.

By default, :sip:ref:`~PyQt6.QtGui.QInputDevice.capabilities` are ``None``.

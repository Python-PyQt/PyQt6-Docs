.. sip:method-description::
    :status: todo
    :pysig: f4ab4e7d53da19a404f41a8ee0f96f1d
    :realsig: (const QString&)
    :digest: af7c8a71a7cfb48a2ca66dd5fc88de7d

Returns the primary pointing device (the core pointer, traditionally assumed to be a mouse) on the given seat *seatName*.

If multiple pointing devices are registered, this function prefers a mouse or touchpad that matches the given *seatName* and that does not have another device as its parent. Usually only one master or core device does not have a parent device. But if such a device is not found, this function creates a new virtual "core pointer" mouse. Thus Qt continues to work on platforms that are not yet doing input device discovery and registration.

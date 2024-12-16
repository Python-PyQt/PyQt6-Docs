.. sip:method-description::
    :status: todo
    :pysig: 3905f6675f143f0f6a1efe899e90d8c1
    :realsig: ()
    :digest: 01fd813332c1f93b1686d5d70cb52afc

Returns a list of all registered input devices (keyboards and pointing devices).

**Note:** The list of devices is not always complete on all platforms. So far, the most-complete information is available on the X11 platform, at startup and in response to hot-plugging. Most other platforms are only able to provide generic devices of various types, only after receiving events from them; and most platforms do not tell Qt when a device is plugged in, or when it is unplugged at runtime.

**Note:** The returned list cannot be used to add new devices. To add a simulated touch screen for an autotest, QTest::createTouchDevice() can be used. Platform plugins should call QWindowSystemInterface::registerInputDevice() to add devices as they are discovered.

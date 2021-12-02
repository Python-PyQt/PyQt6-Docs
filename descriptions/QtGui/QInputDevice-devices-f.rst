.. sip:method-description::
    :status: todo
    :pysig: 85ab5de8365213122415b547be716786
    :realsig: ()
    :digest: f2a2b505d9689a7ce650347cccc2ab55

Returns a list of all registered input devices (keyboards and pointing devices).

**Note:** The returned list cannot be used to add new devices. To add a simulated touch screen for an autotest, QTest::createTouchDevice() can be used. Platform plugins should call  to add devices as they are discovered.

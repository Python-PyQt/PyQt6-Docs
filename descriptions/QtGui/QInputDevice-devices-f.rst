.. sip:method-description::
    :status: todo
    :pysig: 85ab5de8365213122415b547be716786
    :realsig: ()
    :digest: 3b125cdc7f1c2f1bad2d3978d0eecc98

Returns a list of all registered input devices (keyboards and pointing devices).

**Note:** The returned list cannot be used to add new devices. To add a simulated touch screen for an autotest,  can be used. Platform plugins should call  to add devices as they are discovered.

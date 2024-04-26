.. sip:method-description::
    :status: todo
    :pysig: 394200b40df23d07efe9586de9a39591
    :realsig: () const
    :digest: 0a901b2bac9034c87fafc7cc9aa5aaa6

Returns the default audio format settings for this device.

These settings are provided by the platform/audio plugin being used.

They are also dependent on the QtAudio::Mode being used.

A typical audio system would provide something like:

* Input settings: 48000Hz mono 16 bit.

* Output settings: 48000Hz stereo 16 bit.

.. sip:method-description::
    :status: todo
    :pysig: 394200b40df23d07efe9586de9a39591
    :realsig: () const
    :digest: 4955a9b9ddd0910b80b3812bd91af1c1

Returns the default audio format settings for this device.

These settings are provided by the platform/audio plugin being used.

They are also dependent on the :sip:ref:`~PyQt6.QtMultimedia.QAudio`::Mode being used.

A typical audio system would provide something like:

* Input settings: 48000Hz mono 16 bit.

* Output settings: 48000Hz stereo 16 bit.

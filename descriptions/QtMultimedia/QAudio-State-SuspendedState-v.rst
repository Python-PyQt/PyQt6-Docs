.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 6fbe434312bcca609f0fd906c15a002a

The audio stream is in a suspended state. Entered after suspend() is called or when another stream takes control of the audio device. In the later case, a call to resume will return control of the audio device to this stream. This should usually only be done upon user request.

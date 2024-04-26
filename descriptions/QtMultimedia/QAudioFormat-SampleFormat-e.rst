.. sip:enum-description::
    :status: todo
    :digest: aa06afaad3b51d4f97f32425ff347759

Qt will always expect and use samples in the endianness of the host platform. When processing audio data from external sources yourself, ensure you convert them to the correct endianness before writing them to a :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` or :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer`.

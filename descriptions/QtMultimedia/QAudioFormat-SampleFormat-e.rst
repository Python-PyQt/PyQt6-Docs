.. sip:enum-description::
    :status: todo
    :digest: c75b2847f983a00d1c3819d5d4c95270

Qt will always expect and use samples in the endianness of the host platform. When processing audio data from external sources yourself, ensure you convert them to the correct endianness before writing them to a QAudioSink or QAudioBuffer.

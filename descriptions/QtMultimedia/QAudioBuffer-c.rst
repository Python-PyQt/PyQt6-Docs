.. sip:class-description::
    :status: todo
    :brief: Represents a collection of audio samples with a specific format and sample rate
    :digest: 6e83c0c50dbc7e4832f2d0f10277656d

The :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer` class represents a collection of audio samples with a specific format and sample rate.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer` is used by the :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder` class to hand decoded audio data over to the application. An audio buffer contains data in a certain :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` that can be queried using :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.format`. It is also tagged with timing and duration information.

To access the data stored inside the buffer, use the :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.data` or :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.constData` methods.

Audio buffers are explicitly shared, in most cases, you should call :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.detach` before modifying the data.

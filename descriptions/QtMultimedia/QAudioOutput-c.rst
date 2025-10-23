.. sip:class-description::
    :status: todo
    :brief: Represents an output channel for audio
    :digest: 46b51200279f9c9085a8fdefbd81dd8b

Represents an output channel for audio.

This class represents an output channel that can be used together with :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` or :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`. It enables the selection of the physical output device to be used, muting the channel, and changing the channel's volume.

**Note:** On WebAssembly platform, due to it's asynchronous nature, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.audioOutputsChanged` signal is emitted when the list of audio outputs is ready. User permissions are required. Works only on secure https contexts.

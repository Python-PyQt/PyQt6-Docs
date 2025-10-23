.. sip:class-description::
    :status: todo
    :brief: Represents an input channel for audio
    :digest: e73c44c8b949f371a7da1ba493f08bab

Represents an input channel for audio.

This class represents an input channel that can be used together with :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`. It enables the selection of the physical input device to be used, muting the channel, and changing the channel's volume.

**Note:** On WebAssembly platform, due to it's asynchronous nature, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.audioInputsChanged` signal is emitted when the list of audio inputs is ready. User permissions are required. Works only on secure https contexts.

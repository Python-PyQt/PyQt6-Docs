.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: c54102acc40380e01eccf67d5b954044

Set the output IO device for media content.

The *device* must have been opened in the :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.WriteOnly` or :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite` modes before the recording starts.

The media recorder doesn't take ownership of the specified *device*. If the recording has been started, the device must be kept alive and open until the signal ``recorderStateChanged(StoppedState)`` is emitted.

This method resets :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.actualLocation` immediately unless the specified *device* is ``null``.

If a writable output device is assigned to the recorder, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.outputLocation` is ignored, and :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.actualLocation` is not generated when recording starts. This behavior may change in the future, so we recommend setting only one output, either ``outputLocation`` or ``outputDevice``.

``QMediaRecorder::setOutputDevice`` is only supported with the FFmpeg backend.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.outputDevice`, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.outputLocation`.

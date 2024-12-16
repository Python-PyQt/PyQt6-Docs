.. sip:method-description::
    :status: todo
    :pysig: c42757b033efe678db75a00bb20d0f00
    :realsig: (const QAudioBuffer&)
    :digest: d32511fa93a2ae85623c50eabf6a87ec

Sends :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer` to :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` through :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.

Returns ``true`` if the specified *audioBuffer* has been sent successfully to the destination. Returns ``false``, if the buffer hasn't been sent, which can happen if the instance is not assigned to :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`, the session doesn't have a media recorder, the media recorder is not started or its queue is full. The :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.readyToSendAudioBuffer` signal will be emitted as soon as the destination is able to handle a new audio buffer.

Sending of an empty audio buffer is treated by :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` as an end of the input stream. :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` stops the recording automatically if :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.autoStop` is ``true`` and all the inputs have reported the end of the stream.

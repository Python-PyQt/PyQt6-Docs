.. sip:class-description::
    :status: todo
    :brief: Used for encoding and recording a capture session
    :digest: 2ca4200ba774a4ab161be5cbb233ea49

The :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` class is used for encoding and recording a capture session.

Use the :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` class to encode and record media generated in :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`. You can generate:

* Audio. Use :sip:ref:`~PyQt6.QtMultimedia.QAudioInput` or :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput`.

* Video. Use :sip:ref:`~PyQt6.QtMultimedia.QCamera`, :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture`, :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`, or :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput`.

To record media, connect a generator to a corresponding media capture session.

Performance of video encoding and recording is limited by the hardware, the operating system, the installed graphic drivers, and the input video format. If ``QCamera``, ``QScreenCapture``, or ``QWindowCapture`` produces video frames faster than ``QMediaRecorder`` can encode and record them, the recorder may drop some frames. This is likely to occur if the input frame resolution is high, 4K for example, and hardware-accelerated encoding is unavailable. If you generate input video via ``QVideoFrameInput``, the method ``QVideoFrameInput::sendVideoFrame`` will do nothing and return ``false`` whenever this limitation is reached and the internal frame queue is full. Rely on the signal ``QVideoFrameInput::readyToSendVideoFrame`` to know when the recorder is ready to receive new frames again. If you cannot change the rate of video frame generation and dropping frames is undesirable, we recommend implementing your own frame queue on top of ``QVideoFrameInput``, considering the memory limitations of the hardware.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-media.py
    :lines: 137-144

.. sip:class-description::
    :status: todo
    :brief: Used for providing custom video frames to QMediaRecorder or a video output through QMediaCaptureSession
    :digest: 3b44c63f44c2715d8fec24eb630be12a

The :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput` class is used for providing custom video frames to :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` or a video output through :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.

:sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput` is only supported with the FFmpeg backend.

Custom video frames can be recorded by connecting a :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput` and a :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` to a :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`. For a pull mode implementation, call :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.sendVideoFrame` in response to the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.readyToSendVideoFrame` signal. In the snippet below this is done by connecting the signal to a slot in a custom media generator class. The slot function emits another signal with a new video frame, which is connected to :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.sendVideoFrame`:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-custommediainputsnippets-custommediainputsnippets.py
    :lines: 11-25

Here's a minimal implementation of the slot function that provides video frames:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-custommediainputsnippets-custommediainputsnippets.py
    :lines: 59-63

For more details see :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.readyToSendVideoFrame` and :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.sendVideoFrame`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`, :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`.

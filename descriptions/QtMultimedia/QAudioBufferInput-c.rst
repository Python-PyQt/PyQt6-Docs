.. sip:class-description::
    :status: todo
    :brief: Used for providing custom audio buffers to QMediaRecorder through QMediaCaptureSession
    :digest: 871fbcf6e557028028abff25cd04110a

The :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput` class is used for providing custom audio buffers to :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` through :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput` is only supported with the FFmpeg backend.

Custom audio buffers can be recorded by connecting a :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput` and a :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` to a :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`. For a pull mode implementation, call :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.sendAudioBuffer` in response to the :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.readyToSendAudioBuffer` signal. In the snippet below this is done by connecting the signal to a slot in a custom media generator class. The slot function emits another signal with a new audio buffer, which is connected to :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.sendAudioBuffer`:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-custommediainputsnippets-custommediainputsnippets.py
    :lines: 36-50

Here's a minimal implementation of the slot function that provides audio buffers:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-custommediainputsnippets-custommediainputsnippets.py
    :lines: 67-71

For more details see :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.readyToSendAudioBuffer` and :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.sendAudioBuffer`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.

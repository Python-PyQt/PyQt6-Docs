.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c6a0431906bc6bb0a774b4fd17a71827

Start recording.

While the recorder state is changed immediately to c{\ :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.RecorderState.RecordingState`}, recording may start asynchronously.

If recording fails :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.error` signal is emitted with recorder state being reset back to ``QMediaRecorder::StoppedState``.

**Note:** On mobile devices, recording will happen in the orientation the device had when calling record and is locked for the duration of the recording. To avoid artifacts on the user interface, we recommend to keep the user interface locked to the same orientation as long as the recording is ongoing using the contentOrientation property of :sip:ref:`~PyQt6.QtGui.QWindow` and unlock it again once the recording is finished.

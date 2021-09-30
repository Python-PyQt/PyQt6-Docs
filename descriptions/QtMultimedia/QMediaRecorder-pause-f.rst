.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a36217baadf0b90310c934a547bdcd8c

Pauses recording.

The recorder state is changed to :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.RecorderState.PausedState`.

Depending on the platform, pausing recording may be not supported. In this case the recorder state is unchanged.

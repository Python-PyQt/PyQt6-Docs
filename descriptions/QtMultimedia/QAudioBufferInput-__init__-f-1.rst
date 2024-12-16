.. sip:method-description::
    :status: todo
    :pysig: 48e2d135ac1c542a81adcefb6be62f5a
    :realsig: (const QAudioFormat&, QObject*)
    :digest: d53acd6cfbc5969574fdaf83493f3d01

Constructs a new :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput` object with audio *format* and *parent*.

The specified *format* will work as a hint for the initialization of the matching audio encoder upon invoking :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.record`. If the format is not specified or not valid, the audio encoder will be initialized upon sending the first audio buffer.

We recommend specifying the format if you know in advance what kind of audio buffers you're going to send.

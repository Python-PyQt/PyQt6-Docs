.. sip:method-description::
    :status: todo
    :pysig: 48e2d135ac1c542a81adcefb6be62f5a
    :realsig: (const QAudioFormat&, QObject*)
    :digest: 7caecb67afa30ec6d7534b88d329b4c0

Constructs a new :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` object with audio *format* and *parent*.

If the specified *format* is valid, it will be the format of output audio buffers. Otherwise, the format of output audio buffers will depend on the source media file and the inner audio decoder in :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`.

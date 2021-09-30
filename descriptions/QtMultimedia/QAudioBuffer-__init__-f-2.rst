.. sip:method-description::
    :status: todo
    :pysig: 0001626c8844af8ffd03d886b82feec6
    :realsig: (const QByteArray&,const QAudioFormat&,qint64)
    :digest: 6de129a499103a3d3f1ed23de2fcd7c7

Creates a new audio buffer from the supplied *data*, in the given *format*. The format will determine how the number and sizes of the samples are interpreted from the *data*.

If the supplied *data* is not an integer multiple of the calculated frame size, the excess data will not be used.

This audio buffer will copy the contents of *data*.

*startTime* (in microseconds) indicates when this buffer starts in the stream. If this buffer is not part of a stream, set it to -1.

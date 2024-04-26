.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 00b5a1c32da2c8aeb0b0cc90bf481633

Returns a pointer to this buffer's data. You can only read it.

This method is preferred over the const version of :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.data` to prevent unnecessary copying.

Note that there is no checking done on the format of the audio buffer - this is simply a convenience function.

::

    // With a 16bit sample buffer:
    const quint16 *data = buffer->constData<quint16>();

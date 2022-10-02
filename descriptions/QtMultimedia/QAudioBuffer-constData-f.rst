.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: b0ef2560c9bbd574a4a83d155770b8f6

Returns a pointer to this buffer's data. You can only read it.

This method is preferred over the const version of :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.data` to prevent unnecessary copying.

There is also a templatized version of this constData() function that allows you to retrieve a specific type of read-only pointer to the data. Note that there is no checking done on the format of the audio buffer - this is simply a convenience function.

::

    // With a 16bit sample buffer:
    const quint16 *data = buffer->constData<quint16>();

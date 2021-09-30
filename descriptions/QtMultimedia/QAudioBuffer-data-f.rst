.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: ()
    :digest: 2ff9268e790e3727921ed577514a27f9

Returns a pointer to this buffer's data. You can modify the data through the returned pointer.

Since :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer` objects are explicitly shared, you should usually call :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.detach` before modifying the data through this function.

There is also a templatized version of :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.data` allows you to retrieve a specific type of pointer to the data. Note that there is no checking done on the format of the audio buffer - this is simply a convenience function.

::

    // With a 16bit sample buffer:
    quint16 *data = buffer->data<quint16>(); // May cause deep copy

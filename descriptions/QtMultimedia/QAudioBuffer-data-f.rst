.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: ()
    :digest: b98d502e876b65a3b7d898e5e25272cf

Returns a pointer to this buffer's data. You can modify the data through the returned pointer.

Since :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer` objects are explicitly shared, you should usually call :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.detach` before modifying the data through this function.

Note that there is no checking done on the format of the audio buffer - this is simply a convenience function.

::

    // With a 16bit sample buffer:
    quint16 *data = buffer->data<quint16>(); // May cause deep copy

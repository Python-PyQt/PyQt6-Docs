.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4e0a0b88f433111773e1e5e57c9b4edd

Signals that a new audio buffer can be sent to the audio buffer input. After receiving the signal, if you have audio date to be sent, invoke :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.sendAudioBuffer` once or in a loop until it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferInput.sendAudioBuffer`.

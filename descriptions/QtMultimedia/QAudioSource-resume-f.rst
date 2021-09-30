.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cdab58703605efd28a007f231ce1727c

Resumes processing audio data after a :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.suspend`.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error.NoError`. Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.ActiveState` if you previously called start(\ :sip:ref:`~PyQt6.QtCore.QIODevice`\*). Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.IdleState` if you previously called :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`. emits :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal.

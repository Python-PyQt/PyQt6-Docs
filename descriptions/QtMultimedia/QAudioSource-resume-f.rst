.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e26cbfe10b4d17caf57501b0395a8ceb

Resumes processing audio data after a :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.suspend`.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` to QtAudio::NoError. Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` to QtAudio::ActiveState if you previously called start(\ :sip:ref:`~PyQt6.QtCore.QIODevice`\*). Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` to QtAudio::IdleState if you previously called :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`. emits :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal.

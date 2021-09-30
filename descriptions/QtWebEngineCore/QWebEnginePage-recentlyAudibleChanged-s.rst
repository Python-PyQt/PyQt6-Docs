.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 23e54c186e13c6468cb7b0b6d0f20853

This signal is emitted when the page's audible state, *recentlyAudible*, changes, because the audio is played or stopped.

**Note:** The signal is also emitted when calling the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setAudioMuted` method. Also, if the audio is paused, this signal is emitted with an approximate **two-second delay**, from the moment the audio is paused.

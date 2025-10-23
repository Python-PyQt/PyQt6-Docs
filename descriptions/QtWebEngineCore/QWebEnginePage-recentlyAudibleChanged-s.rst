.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: ffb593055301fa7e68f308d28a916cbc

This signal is emitted when the page's audible state, *recentlyAudible*, changes due to audio being played or stopped.

**Note:** The signal is also emitted when the audioMuted property changes. Also, if the audio is paused this signal is emitted with an approximate **two-second delay** from the moment the audio is paused.

If a web page contains two videos that are started in sequence, this signal gets emitted only once, for the first video to generate sound. After both videos are stopped, the signal is emitted upon the last sound generated. This means that the signal is emitted both when any kind of sound is generated and when everything is completely silent within a web page, regardless of the number of audio streams.

Spurious signal emissions might also happen. For example, when sound is stopped, this signal gets emitted first with a value of ``true``, and then with a value of ``false``. Further, when audio starts playing, the signal is emitted twice with a value of ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.recentlyAudible`.

.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e19e8f1665a57b269a9f3a4b28e57889

Signals that the job execution has finished (be it successfully, because an error happened or because it was cancelled).

**Note:** Emission of this signal must be the final action the response performs: once the signal is received, the response will subsequently be destroyed by the engine.

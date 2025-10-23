.. sip:method-description::
    :status: todo
    :pysig: 310ec6a2fe4ba2639c226ebbdc6a0928
    :realsig: (const QAudioDevice&,const QAudioFormat&,QObject*)
    :digest: 0fa671a65ad76fedac7ab0dd21d0d1c4

Construct a new audio input and attach it to *parent*. The device referenced by *audioDevice* is used with the input *format* parameters. If *format* is default-initialized, the format will be set to the preferred format of *audioDevice*.

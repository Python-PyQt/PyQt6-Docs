.. sip:method-description::
    :status: todo
    :pysig: 310ec6a2fe4ba2639c226ebbdc6a0928
    :realsig: (const QAudioDevice&,const QAudioFormat&,QObject*)
    :digest: 439e5f0efd76f543ece2ada42749908a

Construct a new audio output and attach it to *parent*. The device referenced by *audioDevice* is used with the output *format* parameters. If *format* is default-initialized, the format will be set to the preferred format of *audioDevice*.

.. sip:method-description::
    :status: todo
    :pysig: 17b4f95f110a9bb6ff3aab0049947f61
    :realsig: (QCameraDevice::Position,QObject*)
    :digest: de629de6646f4f519c16245f20918955

Construct a :sip:ref:`~PyQt6.QtMultimedia.QCamera` which uses a hardware camera located a the specified *position*.

For example on a mobile phone it can be used to easily choose between front-facing and back-facing cameras.

If no camera is available at the specified *position* or if *position* is :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice.Position.UnspecifiedPosition`, the default camera is used.

.. sip:method-description::
    :status: todo
    :pysig: 2ff0bc9a01c56e2c9899cb3d4aac86e3
    :realsig: (QMediaFormat::ResolveFlags)
    :digest: 35cbd0e9670b986613c44229f55d9393

Resolves the format, based on *flags*, to a format that is supported by :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`.

This method tries to find the best possible match for unspecified settings. Settings that are not supported by the recorder will be modified to the closest match that is supported.

When resolving, priority is given in the following order:

#. File format

#. Video codec

#. Audio codec

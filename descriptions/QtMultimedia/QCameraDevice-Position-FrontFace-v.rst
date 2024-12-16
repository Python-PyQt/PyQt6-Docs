.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 226aa4145d349c456b9982706dd25662

The camera is on the front face of the system hardware. For example on a mobile device, it means it is on the same side as that of the screen. Front-facing cameras generate video frames with the property :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mirrored` set to ``true``. This means that the presentation of these frames is flipped around the vertical axis to display the video output as a mirror, whereas recording only considers the transformations of the surface specified in :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.surfaceFormat`.

.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: b6e6289e491c966448248e9da8527624

Converts current video frame to image.

The conversion is based on the current pixel data and the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.surfaceFormat`. Transformations of the frame don't impact the result since they are applied for presentation only.

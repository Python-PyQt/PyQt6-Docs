.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: 2bb00169b4768bb89f3d3e0dd564329c

Converts current video frame to image.

The consversion is based on the current pixel data and the QVideoFrame::surfaceFormat. Transformations of the frame don't impact the result since they are applied for presentation only.

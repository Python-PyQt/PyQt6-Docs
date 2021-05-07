.. sip:method-description::
    :status: todo
    :pysig: 53226ed3999d12439037f496d7de5d37
    :realsig: (int,const QSize&)
    :digest: 5882eefd65e922df8751daa08a4b0424

Renders current frame to an image of *imageSize*. Default size is the window size. Image is rendered with antialiasing level given in *msaaSamples*. Default level is ``0``.

Returns the rendered image.

**Note:** OpenGL ES2 does not support anitialiasing, so *msaaSamples* is always forced to ``0``.

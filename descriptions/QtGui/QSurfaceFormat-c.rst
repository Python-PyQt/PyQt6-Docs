.. sip:class-description::
    :status: todo
    :brief: Represents the format of a QSurface
    :digest: 11a87f64c277f9627b088def64e38aa4

The :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` class represents the format of a :sip:ref:`~PyQt6.QtGui.QSurface`.

The format includes the size of the color buffers, red, green, and blue; the size of the alpha buffer; the size of the depth and stencil buffers; and number of samples per pixel for multisampling. In addition, the format contains surface configuration parameters such as OpenGL profile and version for rendering, whether or not to enable stereo buffers, and swap behaviour.

**Note:** When troubleshooting context or window format issues, it can be helpful to enable the logging category ``qt.qpa.gl``. Depending on the platform, this may print useful debug information when it comes to OpenGL initialization and the native visual or framebuffer configurations which :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` gets mapped to.

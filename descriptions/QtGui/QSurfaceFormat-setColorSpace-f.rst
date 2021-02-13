.. sip:method-description::
    :status: todo
    :pysig: a16fc74df0b4b43d65e125206b1c2796
    :realsig: (const QColorSpace&)
    :digest: 4fd82eb89a38366fb2c19be3f131b921

Sets the preferred *colorSpace*.

For example, this allows requesting windows with default framebuffers that are sRGB-capable on platforms that support it.

**Note:** When the requested color space is not supported by the platform, the request is ignored. Query the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` after window creation to verify if the color space request could be honored or not.

**Note:** This setting controls if the default framebuffer of the window is capable of updates and blending in a given color space. It does not change applications' output by itself. The applications' rendering code will still have to opt in via the appropriate OpenGL calls to enable updates and blending to be performed in the given color space instead of using the standard linear operations.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.colorSpace`.

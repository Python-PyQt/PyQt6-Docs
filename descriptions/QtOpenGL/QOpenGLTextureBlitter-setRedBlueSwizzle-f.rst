.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b68fa4ee2fad4293d1ec78d101cfa6b4

Sets whether swizzling is enabled for the red and blue color channels to *swizzle*. An BGRA to RGBA conversion (occurring in the shader on the GPU, instead of a slow CPU-side transformation) can be useful when the source texture contains data from a :sip:ref:`~PyQt6.QtGui.QImage` with a format like :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32` which maps to BGRA on little endian systems.

By default the red-blue swizzle is disabled since this is what a texture attached to an framebuffer object or a texture based on a byte ordered :sip:ref:`~PyQt6.QtGui.QImage` format (like :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGBA8888`) needs.

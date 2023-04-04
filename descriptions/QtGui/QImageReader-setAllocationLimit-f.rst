.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (int)
    :digest: 09d8e32f0ce4353d18e42a8792c4c721

Sets the allocation limit to *mbLimit* megabytes. Images that would require a :sip:ref:`~PyQt6.QtGui.QImage` memory allocation above this limit will be rejected. If *mbLimit* is 0, the allocation size check will be disabled.

This limit helps applications avoid unexpectedly large memory usage from loading corrupt image files. It is normally not needed to change it. The default limit is large enough for all commonly used image sizes.

**Note:** The memory requirements are calculated for a minimum of 32 bits per pixel, since Qt will typically convert an image to that depth when it is used in GUI. This means that the effective allocation limit is significantly smaller than *mbLimit* when reading 1 bpp and 8 bpp images.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.allocationLimit`.

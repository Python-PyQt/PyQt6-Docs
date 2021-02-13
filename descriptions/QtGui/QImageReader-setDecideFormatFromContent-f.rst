.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 911173b35f57afbc6306c7ff0fdb82f5

If *ignored* is set to true, then the image reader will ignore specified formats or file extensions and decide which plugin to use only based on the contents in the datastream.

Setting this flag means that all image plugins gets loaded. Each plugin will read the first bytes in the image data and decide if the plugin is compatible or not.

This also disables auto detecting the image format.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.decideFormatFromContent`.

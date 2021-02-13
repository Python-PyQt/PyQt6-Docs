.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: cedc4708eb0f5015ba468c83ce4189d8

The scaled clip rect (or ROI, Region Of Interest) of the image. A handler that supports this option is expected to apply the provided clip rect (a :sip:ref:`~PyQt6.QtCore.QRect`), after applying any scaling (ScaleSize) or regular clipping (). If the handler does not support this option, :sip:ref:`~PyQt6.QtGui.QImageReader` will apply the scaled clip rect after the image has been read.

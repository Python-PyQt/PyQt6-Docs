.. sip:enum-description::
    :status: todo
    :digest: 76356d3d452e277c54230a4c70a6d08b

This enum is used to describe the features or capabilities that the paint engine has. If a feature is not supported by the engine, :sip:ref:`~PyQt6.QtGui.QPainter` will do a best effort to emulate that feature through other means and pass on an alpha blended :sip:ref:`~PyQt6.QtGui.QImage` to the engine with the emulated results. Some features cannot be emulated:  and .

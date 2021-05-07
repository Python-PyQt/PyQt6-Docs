.. sip:enum-description::
    :status: todo
    :digest: 846f16ae86ecc1bbdd8c85334aff0bdb

This enum is used to describe the features or capabilities that the paint engine has. If a feature is not supported by the engine, :sip:ref:`~PyQt6.QtGui.QPainter` will do a best effort to emulate that feature through other means and pass on an alpha blended :sip:ref:`~PyQt6.QtGui.QImage` to the engine with the emulated results. Some features cannot be emulated:  and .

.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: d8d216441210ff51b22f614e996eac9c

Sets the timeline's frame counter to start at *startFrame*, and end and *endFrame*. For each time value, :sip:ref:`~PyQt6.QtCore.QTimeLine` will find the corresponding frame when you call :sip:ref:`~PyQt6.QtCore.QTimeLine.currentFrame` or :sip:ref:`~PyQt6.QtCore.QTimeLine.frameForTime` by interpolating, using the return value of :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime`.

When in Running state, :sip:ref:`~PyQt6.QtCore.QTimeLine` also emits the :sip:ref:`~PyQt6.QtCore.QTimeLine.frameChanged` signal when the frame changes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.startFrame`, :sip:ref:`~PyQt6.QtCore.QTimeLine.endFrame`, :sip:ref:`~PyQt6.QtCore.QTimeLine.start`, :sip:ref:`~PyQt6.QtCore.QTimeLine.currentFrame`.

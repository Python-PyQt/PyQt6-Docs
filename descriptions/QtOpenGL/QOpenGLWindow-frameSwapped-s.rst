.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e192946442e8cccbf60eee07ba0221f2

This signal is emitted after the potentially blocking :sip:ref:`~PyQt6.QtGui.QOpenGLContext.swapBuffers` has been done. Applications that wish to continuously repaint synchronized to the vertical refresh, should issue an update() upon this signal. This allows for a much smoother experience compared to the traditional usage of timers.

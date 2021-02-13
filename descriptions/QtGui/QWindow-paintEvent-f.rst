.. sip:method-description::
    :status: todo
    :pysig: f2ec3c5d78a75ad8f7dac6730db95648
    :realsig: (QPaintEvent*)
    :digest: bac4f33fe8c8597c2fa8b0e00f1b0f58

The paint event (\ *ev*) is sent by the window system whenever an area of the window needs a repaint, for example when initially showing the window, or due to parts of the window being uncovered by moving another window.

The application is expected to render into the window in response to the paint event, regardless of the exposed state of the window. For example, a paint event may be sent before the window is exposed, to prepare it for showing to the user.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent`.

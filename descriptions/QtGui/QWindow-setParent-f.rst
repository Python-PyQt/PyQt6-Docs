.. sip:method-description::
    :status: todo
    :pysig: 72e2cafa091a7d38d145ec5a6e8cba39
    :realsig: (QWindow*)
    :digest: f4846bdf137fef08d4341f17d0fd01ad

Sets the *parent* Window. This will lead to the windowing system managing the clip of the window, so it will be clipped to the *parent* window.

Setting *parent* to be ``nullptr`` will make the window become a top level window.

If *parent* is a window created by :sip:ref:`~PyQt6.QtGui.QWindow.fromWinId`, then the current window will be embedded inside *parent*, if the platform supports it.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.parent`.

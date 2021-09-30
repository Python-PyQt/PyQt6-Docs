.. sip:signal-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: (const QRect&)
    :digest: 5788de34b6f72c443656d7f0d0073176

This signal is emitted whenever the document wants to change the position and size of the page to *geom*. This can happen for example through JavaScript.

**Note:** :sip:ref:`~PyQt6.QtGui.QWindow.setGeometry` expects a size excluding the window decoration, while *geom* includes it. You have to remove the size of the frame margins from *geom* to handle this signal correctly.

::

    window->setGeometry(geom.marginsRemoved(window->frameMargins()));

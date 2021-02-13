.. sip:class-description::
    :status: todo
    :brief: Abstract base class for QIcon renderers
    :digest: a29752139f5ef4883515656e3028fbfc

The :sip:ref:`~PyQt6.QtGui.QIconEngine` class provides an abstract base class for :sip:ref:`~PyQt6.QtGui.QIcon` renderers.

An icon engine provides the rendering functions for a :sip:ref:`~PyQt6.QtGui.QIcon`. Each icon has a corresponding icon engine that is responsible for drawing the icon with a requested size, mode and state.

The icon is rendered by the :sip:ref:`~PyQt6.QtGui.QIconEngine.paint` function, and the icon can additionally be obtained as a pixmap with the :sip:ref:`~PyQt6.QtGui.QIconEngine.pixmap` function (the default implementation simply uses :sip:ref:`~PyQt6.QtGui.QIconEngine.paint` to achieve this). The :sip:ref:`~PyQt6.QtGui.QIconEngine.addPixmap` function can be used to add new pixmaps to the icon engine, and is used by :sip:ref:`~PyQt6.QtGui.QIcon` to add specialized custom pixmaps.

The :sip:ref:`~PyQt6.QtGui.QIconEngine.paint`, :sip:ref:`~PyQt6.QtGui.QIconEngine.pixmap`, and :sip:ref:`~PyQt6.QtGui.QIconEngine.addPixmap` functions are all virtual, and can therefore be reimplemented in subclasses of :sip:ref:`~PyQt6.QtGui.QIconEngine`.

.. seealso:: QIconEnginePlugin.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d597718d0681afc33762191ab73c5ab3

Allocates the platform resources associated with the window.

It is at this point that the surface format set using :sip:ref:`~PyQt6.QtGui.QWindow.setFormat` gets resolved into an actual native surface. However, the window remains hidden until :sip:ref:`~PyQt6.QtGui.QWindow.setVisible` is called.

Note that it is not usually necessary to call this function directly, as it will be implicitly called by :sip:ref:`~PyQt6.QtGui.QWindow.show`, :sip:ref:`~PyQt6.QtGui.QWindow.setVisible`, :sip:ref:`~PyQt6.QtGui.QWindow.winId`, and other functions that require access to the platform resources.

Call :sip:ref:`~PyQt6.QtGui.QWindow.destroy` to free the platform resources if necessary.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.destroy`.

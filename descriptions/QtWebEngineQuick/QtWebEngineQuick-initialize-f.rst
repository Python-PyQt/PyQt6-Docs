.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: 22e19b1a823df633e2f030d1ca455a62

Sets up an OpenGL Context that can be shared between threads. This has to be done before :sip:ref:`~PyQt6.QtGui.QGuiApplication` is created and before window's QPlatformOpenGLContext is created.

This has the same effect as setting the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` attribute with :sip:ref:`~PyQt6.QtCore.QCoreApplication.setAttribute` before constructing :sip:ref:`~PyQt6.QtGui.QGuiApplication`.

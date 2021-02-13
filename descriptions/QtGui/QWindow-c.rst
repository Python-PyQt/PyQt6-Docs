.. sip:class-description::
    :status: todo
    :brief: Represents a window in the underlying windowing system
    :digest: 0870f80db1c88f291fcea5a09ab5a93d

The :sip:ref:`~PyQt6.QtGui.QWindow` class represents a window in the underlying windowing system.

A window that is supplied a parent becomes a native child window of their parent window.

An application will typically use `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or QQuickView for its UI, and not :sip:ref:`~PyQt6.QtGui.QWindow` directly. Still, it is possible to render directly to a :sip:ref:`~PyQt6.QtGui.QWindow` with :sip:ref:`~PyQt6.QtGui.QBackingStore` or `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_, when wanting to keep dependencies to a minimum or when wanting to use OpenGL directly. The `Raster Window Example <https://doc.qt.io/qt-6/qtgui-rasterwindow-example.html>`_ and OpenGL Window Example are useful reference examples for how to render to a :sip:ref:`~PyQt6.QtGui.QWindow` using either approach.

.. _qwindow-resource-management:

Resource Management
-------------------

Windows can potentially use a lot of memory. A usual measurement is width times height times color depth. A window might also include multiple buffers to support double and triple buffering, as well as depth and stencil buffers. To release a window's memory resources, call the :sip:ref:`~PyQt6.QtGui.QWindow.destroy` function.

.. _qwindow-content-orientation:

Content Orientation
-------------------

:sip:ref:`~PyQt6.QtGui.QWindow` has :sip:ref:`~PyQt6.QtGui.QWindow.reportContentOrientationChange` that can be used to specify the layout of the window contents in relation to the screen. The content orientation is simply a hint to the windowing system about which orientation the window contents are in. It's useful when you wish to keep the same window size, but rotate the contents instead, especially when doing rotation animations between different orientations. The windowing system might use this value to determine the layout of system popups or dialogs.

.. _qwindow-visibility-and-windowing-system-exposure:

Visibility and Windowing System Exposure
----------------------------------------

By default, the window is not visible, and you must call :sip:ref:`~PyQt6.QtGui.QWindow.setVisible`\ (true), or :sip:ref:`~PyQt6.QtGui.QWindow.show` or similar to make it visible. To make a window hidden again, call :sip:ref:`~PyQt6.QtGui.QWindow.setVisible`\ (false) or :sip:ref:`~PyQt6.QtGui.QWindow.hide`. The visible property describes the state the application wants the window to be in. Depending on the underlying system, a visible window might still not be shown on the screen. It could, for instance, be covered by other opaque windows or moved outside the physical area of the screen. On windowing systems that have exposure notifications, the :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` accessor describes whether the window should be treated as directly visible on screen. The :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent` function is called whenever an area of the window is invalidated, for example due to the exposure in the windowing system changing. On windowing systems that do not make this information visible to the application, :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` will simply return the same value as :sip:ref:`~PyQt6.QtGui.QWindow.isVisible`.

:sip:ref:`~PyQt6.QtGui.QWindow.Visibility` queried through :sip:ref:`~PyQt6.QtGui.QWindow.visibility` is a convenience API combining the functions of visible() and :sip:ref:`~PyQt6.QtGui.QWindow.windowStates`.

.. _qwindow-rendering:

Rendering
---------

There are two Qt APIs that can be used to render content into a window, :sip:ref:`~PyQt6.QtGui.QBackingStore` for rendering with a :sip:ref:`~PyQt6.QtGui.QPainter` and flushing the contents to a window with type :sip:ref:`~PyQt6.QtGui.QSurface.SurfaceType.RasterSurface`, and `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ for rendering with OpenGL to a window with type :sip:ref:`~PyQt6.QtGui.QSurface.SurfaceType.OpenGLSurface`.

The application can start rendering as soon as :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` returns ``true``, and can keep rendering until it :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` returns ``false``. To find out when :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` changes, reimplement :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent`. The window will always get a resize event before the first expose event.

.. _qwindow-initial-geometry:

Initial Geometry
----------------

If the window's width and height are left uninitialized, the window will get a reasonable default geometry from the platform window. If the position is left uninitialized, then the platform window will allow the windowing system to position the window. For example on X11, the window manager usually does some kind of smart positioning to try to avoid having new windows completely obscure existing windows. However :sip:ref:`~PyQt6.QtGui.QWindow.setGeometry` initializes both the position and the size, so if you want a fixed size but an automatic position, you should call :sip:ref:`~PyQt6.QtGui.QWindow.resize` or :sip:ref:`~PyQt6.QtGui.QWindow.setWidth` and :sip:ref:`~PyQt6.QtGui.QWindow.setHeight` instead.

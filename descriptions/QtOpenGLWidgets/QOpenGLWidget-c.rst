.. sip:class-description::
    :status: todo
    :brief: Widget for rendering OpenGL graphics
    :digest: fab812cf58dc00d815d88ae6d3ecd8a9

The :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` class is a widget for rendering OpenGL graphics.

:sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` provides functionality for displaying OpenGL graphics integrated into a Qt application. It is very simple to use: Make your class inherit from it and use the subclass like any other :sip:ref:`~PyQt6.QtWidgets.QWidget`, except that you have the choice between using :sip:ref:`~PyQt6.QtGui.QPainter` and standard OpenGL rendering commands.

:sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` provides three convenient virtual functions that you can reimplement in your subclass to perform the typical OpenGL tasks:

* :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` - Renders the OpenGL scene. Gets called whenever the widget needs to be updated.

* :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL` - Sets up the OpenGL viewport, projection, etc. Gets called whenever the widget has been resized (and also when it is shown for the first time because all newly created widgets get a resize event automatically).

* :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` - Sets up the OpenGL resources and state. Gets called once before the first time :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL` or :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` is called.

If you need to trigger a repaint from places other than :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` (a typical example is when using :sip:ref:`~PyQt6.QtCore.QTimer` to animate scenes), you should call the widget's update() function to schedule an update.

Your widget's OpenGL rendering context is made current when :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL`, or :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` is called. If you need to call the standard OpenGL API functions from other places (e.g. in your widget's constructor or in your own paint functions), you must call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` first.

All rendering happens into an OpenGL framebuffer object. :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` ensure that it is bound in the context. Keep this in mind when creating and binding additional framebuffer objects in the rendering code in :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`. Never re-bind the framebuffer with ID 0. Instead, call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.defaultFramebufferObject` to get the ID that should be bound.

:sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` allows using different OpenGL versions and profiles when the platform supports it. Just set the requested format via :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`. Keep in mind however that having multiple :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances in the same window requires that they all use the same format, or at least formats that do not make the contexts non-sharable. To overcome this issue, prefer using :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` instead of :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`.

**Note:** Calling :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` before constructing the :sip:ref:`~PyQt6.QtWidgets.QApplication` instance is mandatory on some platforms (for example, macOS) when an OpenGL core profile context is requested. This is to ensure that resource sharing between contexts stays functional as all internal contexts are created using the correct version and profile.

.. _qopenglwidget-painting-techniques:

Painting Techniques
-------------------

As described above, subclass :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` to render pure 3D content in the following way:

* Reimplement the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` and :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL` functions to set up the OpenGL state and provide a perspective transformation.

* Reimplement :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` to paint the 3D scene, calling only OpenGL functions.

It is also possible to draw 2D graphics onto a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` subclass using :sip:ref:`~PyQt6.QtGui.QPainter`:

* In :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, instead of issuing OpenGL commands, construct a :sip:ref:`~PyQt6.QtGui.QPainter` object for use on the widget.

* Draw primitives using :sip:ref:`~PyQt6.QtGui.QPainter`'s member functions.

* Direct OpenGL commands can still be issued. However, you must make sure these are enclosed by a call to the painter's beginNativePainting() and endNativePainting().

When performing drawing using :sip:ref:`~PyQt6.QtGui.QPainter` only, it is also possible to perform the painting like it is done for ordinary widgets: by reimplementing :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintEvent`.

* Reimplement the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintEvent` function.

* Construct a :sip:ref:`~PyQt6.QtGui.QPainter` object targeting the widget. Either pass the widget to the constructor or the :sip:ref:`~PyQt6.QtGui.QPainter.begin` function.

* Draw primitives using :sip:ref:`~PyQt6.QtGui.QPainter`'s member functions.

* Painting finishes then the :sip:ref:`~PyQt6.QtGui.QPainter` instance is destroyed. Alternatively, call :sip:ref:`~PyQt6.QtGui.QPainter.end` explicitly.

.. _qopenglwidget-opengl-function-calls-headers-and-qopenglfunctions:

OpenGL Function Calls, Headers and QOpenGLFunctions
---------------------------------------------------

When making OpenGL function calls, it is strongly recommended to avoid calling the functions directly. Instead, prefer using QOpenGLFunctions (when making portable applications) or the versioned variants (for example, QOpenGLFunctions_3_2_Core and similar, when targeting modern, desktop-only OpenGL). This way the application will work correctly in all Qt build configurations, including the ones that perform dynamic OpenGL implementation loading which means applications are not directly linking to an GL implementation and thus direct function calls are not feasible.

In :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` the current context is always accessible by caling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.currentContext`. From this context an already initialized, ready-to-be-used QOpenGLFunctions instance is retrievable by calling QOpenGLContext::functions(). An alternative to prefixing every GL call is to inherit from QOpenGLFunctions and call QOpenGLFunctions::initializeOpenGLFunctions() in :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`.

As for the OpenGL headers, note that in most cases there will be no need to directly include any headers like GL.h. The OpenGL-related Qt headers will include qopengl.h which will in turn include an appropriate header for the system. This might be an OpenGL ES 3.x or 2.0 header, the highest version that is available, or a system-provided gl.h. In addition, a copy of the extension headers (called glext.h on some systems) is provided as part of Qt both for OpenGL and OpenGL ES. These will get included automatically on platforms where feasible. This means that constants and function pointer typedefs from ARB, EXT, OES extensions are automatically available.

.. _qopenglwidget-code-examples:

Code Examples
-------------

To get started, the simplest :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` subclass could like like the following:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 54-84

Alternatively, the prefixing of each and every OpenGL call can be avoided by deriving from QOpenGLFunctions instead:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 88-98

To get a context compatible with a given OpenGL version or profile, or to request depth and stencil buffers, call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 102-108

With OpenGL 3.0+ contexts, when portability is not important, the versioned QOpenGLFunctions variants give easy access to all the modern OpenGL functions available in a given version:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 112-120

As described above, it is simpler and more robust to set the requested format globally so that it applies to all windows and contexts during the lifetime of the application. Below is an example of this:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 195-210

.. _qopenglwidget-multisampling:

Multisampling
-------------

To enable multisampling, set the number of requested samples on the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` that is passed to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat`. On systems that do not support it the request may get ignored.

Multisampling support requires support for multisampled renderbuffers and framebuffer blits. On OpenGL ES 2.0 implementations it is likely that these will not be present. This means that multisampling will not be available. With modern OpenGL versions and OpenGL ES 3.0 and up this is usually not a problem anymore.

.. _qopenglwidget-threading:

Threading
---------

Performing offscreen rendering on worker threads, for example to generate textures that are then used in the GUI/main thread in :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`, are supported by exposing the widget's :sip:ref:`~PyQt6.QtGui.QOpenGLContext` so that additional contexts sharing with it can be created on each thread.

Drawing directly to the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s framebuffer outside the GUI/main thread is possible by reimplementing :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintEvent` to do nothing. The context's thread affinity has to be changed via :sip:ref:`~PyQt6.QtCore.QObject.moveToThread`. After that, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` and :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.doneCurrent` are usable on the worker thread. Be careful to move the context back to the GUI/main thread afterwards.

Triggering a buffer swap just for the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` is not possible since there is no real, onscreen native surface for it. It is up to the widget stack to manage composition and buffer swaps on the gui thread. When a thread is done updating the framebuffer, call update() **on the GUI/main thread** to schedule composition.

Extra care has to be taken to avoid using the framebuffer when the GUI/main thread is performing compositing. The signals :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.aboutToCompose` and :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.frameSwapped` will be emitted when the composition is starting and ending. They are emitted on the GUI/main thread. This means that by using a direct connection :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.aboutToCompose` can block the GUI/main thread until the worker thread has finished its rendering. After that, the worker thread must perform no further rendering until the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.frameSwapped` signal is emitted. If this is not acceptable, the worker thread has to implement a double buffering mechanism. This involves drawing using an alternative render target, that is fully controlled by the thread, e.g. an additional framebuffer object, and blitting to the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s framebuffer at a suitable time.

.. _qopenglwidget-context-sharing:

Context Sharing
---------------

When multiple QOpenGLWidgets are added as children to the same top-level widget, their contexts will share with each other. This does not apply for :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances that belong to different windows.

This means that all QOpenGLWidgets in the same window can access each other's sharable resources, like textures, and there is no need for an extra "global share" context.

To set up sharing between :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances belonging to different windows, set the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` application attribute before instantiating :sip:ref:`~PyQt6.QtWidgets.QApplication`. This will trigger sharing between all :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances without any further steps.

Creating extra :sip:ref:`~PyQt6.QtGui.QOpenGLContext` instances that share resources like textures with the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s context is also possible. Simply pass the pointer returned from :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context` to :sip:ref:`~PyQt6.QtGui.QOpenGLContext.setShareContext` before calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.create`. The resulting context can also be used on a different thread, allowing threaded generation of textures and asynchronous texture uploads.

Note that :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` expects a standard conformant implementation of resource sharing when it comes to the underlying graphics drivers. For example, some drivers, in particular for mobile and embedded hardware, have issues with setting up sharing between an existing context and others that are created later. Some other drivers may behave in unexpected ways when trying to utilize shared resources between different threads.

.. _qopenglwidget-resource-initialization-and-cleanup:

Resource Initialization and Cleanup
-----------------------------------

The :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s associated OpenGL context is guaranteed to be current whenever :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` and :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` are invoked. Do not attempt to create OpenGL resources before :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` is called. For example, attempting to compile shaders, initialize vertex buffer objects or upload texture data will fail when done in a subclass's constructor. These operations must be deferred to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`. Some of Qt's OpenGL helper classes, like :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject`, have a matching deferred behavior: they can be instantiated without a context, but all initialization is deferred until a create(), or similar, call. This means that they can be used as normal (non-pointer) member variables in a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` subclass, but the create() or similar function can only be called from :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`. Be aware however that not all classes are designed like this. When in doubt, make the member variable a pointer and create and destroy the instance dynamically in :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` and the destructor, respectively.

Releasing the resources also needs the context to be current. Therefore destructors that perform such cleanup are expected to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` before moving on to destroy any OpenGL resources or wrappers. Avoid deferred deletion via :sip:ref:`~PyQt6.QtCore.QObject.deleteLater` or the parenting mechanism of :sip:ref:`~PyQt6.QtCore.QObject`. There is no guarantee the correct context will be current at the time the instance in question is really destroyed.

A typical subclass will therefore often look like the following when it comes to resource initialization and destruction:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 124-174

This is naturally not the only possible solution. One alternative is to use the :sip:ref:`~PyQt6.QtGui.QOpenGLContext.aboutToBeDestroyed` signal of :sip:ref:`~PyQt6.QtGui.QOpenGLContext`. By connecting a slot, using direct connection, to this signal, it is possible to perform cleanup whenever the underlying native context handle, or the entire :sip:ref:`~PyQt6.QtGui.QOpenGLContext` instance, is going to be released. The following snippet is in principle equivalent to the previous one:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-doc_gui_widgets_qopenglwidget.py
    :lines: 178-191

**Note:** For widgets that change their associated top-level window multiple times during their lifetime, a combined approach is essential. Whenever the widget or a parent of it gets reparented so that the top-level window becomes different, the widget's associated context is destroyed and a new one is created. This is then followed by a call to :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL` where all OpenGL resources must get reinitialized. Due to this the only option to perform proper cleanup is to connect to the context's aboutToBeDestroyed() signal. Note that the context in question may not be the current one when the signal gets emitted. Therefore it is good practice to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` in the connected slot. Additionally, the same cleanup steps must be performed from the derived class' destructor, since the slot connected to the signal will not get invoked when the widget is being destroyed.

**Note:** When :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` is set, the widget's context never changes, not even when reparenting because the widget's associated texture is guaranteed to be accessible also from the new top-level's context.

Proper cleanup is especially important due to context sharing. Even though each :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s associated context is destroyed together with the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, the sharable resources in that context, like textures, will stay valid until the top-level window, in which the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` lived, is destroyed. Additionally, settings like :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` and some Qt modules may trigger an even wider scope for sharing contexts, potentially leading to keeping the resources in question alive for the entire lifetime of the application. Therefore the safest and most robust is always to perform explicit cleanup for all resources and resource wrappers used in the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`.

.. _qopenglwidget-limitations:

Limitations
-----------

Putting other widgets underneath and making the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` transparent will not lead to the expected results: The widgets underneath will not be visible. This is because in practice the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` is drawn before all other regular, non-OpenGL widgets, and so see-through type of solutions are not feasible. Other type of layouts, like having widgets on top of the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, will function as expected.

When absolutely necessary, this limitation can be overcome by setting the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop` attribute on the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`. Be aware however that this breaks stacking order, for example it will not be possible to have other widgets on top of the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, so it should only be used in situations where a semi-transparent :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` with other widgets visible underneath is required.

Note that this does not apply when there are no other widgets underneath and the intention is to have a semi-transparent window. In that case the traditional approach of setting :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_TranslucentBackground` on the top-level window is sufficient. Note that if the transparent areas are only desired in the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, then :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_NoSystemBackground` will need to be turned back to ``false`` after enabling :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_TranslucentBackground`. Additionally, requesting an alpha channel for the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`'s context via :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat` may be necessary too, depending on the system.

:sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` supports multiple update behaviors, just like :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow`. In preserved mode the rendered content from the previous :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` call is available in the next one, allowing incremental rendering. In non-preserved mode the content is lost and :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` implementations are expected to redraw everything in the view.

Before Qt 5.5 the default behavior of :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` was to preserve the rendered contents between :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL` calls. Since Qt 5.5 the default behavior is non-preserved because this provides better performance and the majority of applications have no need for the previous content. This also resembles the semantics of an OpenGL-based :sip:ref:`~PyQt6.QtGui.QWindow` and matches the default behavior of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` in that the color and ancillary buffers are invalidated for each frame. To restore the preserved behavior, call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.setUpdateBehavior` with ``PartialUpdate``.

**Note:** Displaying a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` requires an alpha channel in the associated top-level window's backing store due to the way composition with other :sip:ref:`~PyQt6.QtWidgets.QWidget`-based content works. If there is no alpha channel, the content rendered by the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` will not be visible. This can become particularly relevant on Linux/X11 in remote display setups (such as, with Xvnc), when using a color depth lower than 24. For example, a color depth of 16 will typically map to using a backing store image with the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB16` (RGB565), leaving no room for an alpha channel. Therefore, if experiencing problems with getting the contents of a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` composited correctly with other the widgets in the window, make sure the server (such as, vncserver) is configured with a 24 or 32 bit depth instead of 16.

.. _qopenglwidget-alternatives:

Alternatives
------------

Adding a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` into a window turns on OpenGL-based compositing for the entire window. In some special cases this may not be ideal, and the old QGLWidget-style behavior with a separate, native child window is desired. Desktop applications that understand the limitations of this approach (for example when it comes to overlaps, transparency, scroll views and MDI areas), can use :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow` with :sip:ref:`~PyQt6.QtWidgets.QWidget.createWindowContainer`. This is a modern alternative to QGLWidget and is faster than :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` due to the lack of the additional composition step. It is strongly recommended to limit the usage of this approach to cases where there is no other choice. Note that this option is not suitable for most embedded and mobile platforms, and it is known to have issues on certain desktop platforms (e.g. macOS) too. The stable, cross-platform solution is always :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`.

*OpenGL is a trademark of Silicon Graphics, Inc. in the United States and other countries.*

.. seealso:: QOpenGLFunctions, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow`, :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior.UpdateBehavior`.

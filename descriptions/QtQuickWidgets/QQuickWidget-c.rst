.. sip:class-description::
    :status: todo
    :brief: Widget for displaying a Qt Quick user interface
    :digest: e92e936c9dc2213097ba21357823cfe5

The :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` class provides a widget for displaying a Qt Quick user interface.

This is a convenience wrapper for :sip:ref:`~PyQt6.QtQuick.QQuickWindow` which will automatically load and display a QML scene when given the URL of the main source file. Alternatively, you can instantiate your own objects using :sip:ref:`~PyQt6.QtQml.QQmlComponent` and place them in a manually set up :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`.

Typical usage:

::

    QQuickWidget *view = new QQuickWidget;
    view->setSource(QUrl::fromLocalFile("myqmlfile.qml"));
    view->show();

To receive errors related to loading and executing QML with :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, you can connect to the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.statusChanged` signal and monitor for :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status.Error`. The errors are available via :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.errors`.

:sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` also manages sizing of the view and root object. By default, the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.resizeMode` is :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode.SizeViewToRootObject`, which will load the component and resize it to the size of the view. Alternatively the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.resizeMode` may be set to :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode.SizeRootObjectToView` which will resize the view to the size of the root object.

**Note:** :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` is an alternative to using :sip:ref:`~PyQt6.QtQuick.QQuickView` and :sip:ref:`~PyQt6.QtWidgets.QWidget.createWindowContainer`. The restrictions on stacking order do not apply, making :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` the more flexible alternative, behaving more like an ordinary widget.

**Note:** However, the above mentioned advantages come at the expense of performance. Unlike :sip:ref:`~PyQt6.QtQuick.QQuickWindow` and :sip:ref:`~PyQt6.QtQuick.QQuickView`, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` requires rendering into OpenGL framebuffer objects, which needs to be enforced by calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi`\ (\ :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi.OpenGLRhi`) at startup. This will naturally carry a minor performance hit.

**Note:** Using :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` disables the threaded render loop on all platforms. This means that some of the benefits of threaded rendering, for example `Animator <https://doc.qt.io/qt-6/qml-qtquick-animator.html>`_ classes and vsync driven animations, will not be available.

**Note:** Avoid calling winId() on a :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`. This function triggers the creation of a native window, resulting in reduced performance and possibly rendering glitches. The entire purpose of :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` is to render Quick scenes without a separate native window, hence making it a native widget should always be avoided.

.. _qquickwidget-scene-graph-and-context-persistency:

Scene Graph and Context Persistency
-----------------------------------

:sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` honors :sip:ref:`~PyQt6.QtQuick.QQuickWindow.isPersistentSceneGraph`, meaning that applications can decide - by calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph` on the window returned from the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.quickWindow` function - to let scenegraph nodes and other Qt Quick scene related resources be released whenever the widget becomes hidden. By default persistency is enabled, just like with :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

When running with the OpenGL backend of the scene graph, :sip:ref:`~PyQt6.QtQuick.QQuickWindow` offers the possibility to disable persistent OpenGL contexts as well. This setting is currently ignored by :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` and the context is always persistent. The OpenGL context is thus not destroyed when hiding the widget. The context is destroyed only when the widget is destroyed or when the widget gets reparented into another top-level widget's child hierarchy. However, some applications, in particular those that have their own graphics resources due to performing custom OpenGL rendering in the Qt Quick scene, may wish to disable the latter since they may not be prepared to handle the loss of the context when moving a :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` into another window. Such applications can set the QCoreApplication::AA_ShareOpenGLContexts attribute. For a discussion on the details of resource initialization and cleanup, refer to the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` documentation.

**Note:** :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` offers less fine-grained control over its internal OpenGL context than :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, and there are subtle differences, most notably that disabling the persistent scene graph will lead to destroying the context on a window change regardless of the presence of QCoreApplication::AA_ShareOpenGLContexts.

.. _qquickwidget-limitations:

Limitations
-----------

Putting other widgets underneath and making the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` transparent will not lead to the expected results: the widgets underneath will not be visible. This is because in practice the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` is drawn before all other regular, non-OpenGL widgets, and so see-through types of solutions are not feasible. Other type of layouts, like having widgets on top of the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, will function as expected.

When absolutely necessary, this limitation can be overcome by setting the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop` attribute on the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`. Be aware, however that this breaks stacking order. For example it will not be possible to have other widgets on top of the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, so it should only be used in situations where a semi-transparent :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` with other widgets visible underneath is required.

This limitation only applies when there are other widgets underneath the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` inside the same window. Making the window semi-transparent, with other applications and the desktop visible in the background, is done in the traditional way: Set :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_TranslucentBackground` on the top-level window, request an alpha channel, and change the Qt Quick Scenegraph's clear color to :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.transparent` via :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setClearColor`.

.. _qquickwidget-support-when-not-using-opengl:

Support when not using OpenGL
-----------------------------

In addition to OpenGL, the ``software`` backend of Qt Quick also supports :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`. Other backends, for example OpenVG, are not compatible however and attempting to construct a :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` will lead to problems.

.. _qquickwidget-tab-key-handling:

Tab Key Handling
----------------

On press of the ``[TAB]`` key, the item inside the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` gets focus. If this item can handle ``[TAB]`` key press, focus will change accordingly within the item, otherwise the next widget in the focus chain gets focus.

.. seealso:: `Exposing Attributes of C++ Types to QML <https://doc.qt.io/qt-6/qtqml-cppintegration-exposecppattributes.html>`_, `Qt Quick Widgets Example <https://doc.qt.io/qt-6/qtquick-quickwidgets-quickwidget-example.html>`_, :sip:ref:`~PyQt6.QtQuick.QQuickView`.

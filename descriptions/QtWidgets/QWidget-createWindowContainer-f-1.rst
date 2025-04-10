.. sip:method-description::
    :status: todo
    :pysig: 27c3ecff0b8db6e96a3963b3d763015e
    :realsig: (QWindow*,QWidget*,Qt::WindowFlags)
    :digest: 5d54328b70d32c866f6bf739bcb656f2

Creates a :sip:ref:`~PyQt6.QtWidgets.QWidget` that makes it possible to embed *window* into a :sip:ref:`~PyQt6.QtWidgets.QWidget`-based application.

The window container is created as a child of *parent* and with window flags *flags*.

Once the window has been embedded into the container, the container will control the window's geometry and visibility. Explicit calls to :sip:ref:`~PyQt6.QtGui.QWindow.setGeometry`, :sip:ref:`~PyQt6.QtGui.QWindow.show` or :sip:ref:`~PyQt6.QtGui.QWindow.hide` on an embedded window is not recommended.

The container takes over ownership of *window*. The window can be removed from the window container with a call to :sip:ref:`~PyQt6.QtGui.QWindow.setParent`.

The window container is attached as a native child window to the toplevel window it is a child of. When a window container is used as a child of a :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` or :sip:ref:`~PyQt6.QtWidgets.QMdiArea`, it will create a :ref:`qwidget-native-widgets-vs-alien-widgets` for every widget in its parent chain to allow for proper stacking and clipping in this use case. Creating a native window for the window container also allows for proper stacking and clipping. This must be done before showing the window container. Applications with many native child windows may suffer from performance issues.

The window container has a number of known limitations:

* Stacking order; The embedded window will stack on top of the widget hierarchy as an opaque box. The stacking order of multiple overlapping window container instances is undefined.

* Rendering Integration; The window container does not interoperate with :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`, :sip:ref:`~PyQt6.QtWidgets.QWidget.render` or similar functionality.

* Focus Handling; It is possible to let the window container instance have any focus policy and it will delegate focus to the window via a call to :sip:ref:`~PyQt6.QtGui.QWindow.requestActivate`. However, returning to the normal focus chain from the :sip:ref:`~PyQt6.QtGui.QWindow` instance will be up to the :sip:ref:`~PyQt6.QtGui.QWindow` instance implementation itself. Also, whether :sip:ref:`~PyQt6.QtGui.QWindow.requestActivate` actually gives the window focus, is platform dependent.

  Since 6.8, if embedding a Qt Quick based window, tab presses will transition in and out of the embedded QML window, allowing focus to move to the next or previous focusable object in the window container chain.

* Using many window container instances in a :sip:ref:`~PyQt6.QtWidgets.QWidget`-based application can greatly hurt the overall performance of the application.

* Since 6.7, if *window* belongs to a widget (that is, *window* was received from calling :sip:ref:`~PyQt6.QtWidgets.QWidget.windowHandle`), no container will be created. Instead, this function will return the widget itself, after being reparented to parent. Since no container will be created, *flags* will be ignored. In other words, if *window* belongs to a widget, consider just reparenting that widget to *parent* instead of using this function.

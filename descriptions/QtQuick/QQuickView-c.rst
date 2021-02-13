.. sip:class-description::
    :status: todo
    :brief: Window for displaying a Qt Quick user interface
    :digest: 83fcf4bd734b5b5043d71756e1732ba1

The :sip:ref:`~PyQt6.QtQuick.QQuickView` class provides a window for displaying a Qt Quick user interface.

This is a convenience subclass of :sip:ref:`~PyQt6.QtQuick.QQuickWindow` which will automatically load and display a QML scene when given the URL of the main source file. Alternatively, you can instantiate your own objects using :sip:ref:`~PyQt6.QtQml.QQmlComponent` and place them in a manually setup :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

Typical usage:

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-qquickview-ex.py

To receive errors related to loading and executing QML with :sip:ref:`~PyQt6.QtQuick.QQuickView`, you can connect to the :sip:ref:`~PyQt6.QtQuick.QQuickView.statusChanged` signal and monitor for :sip:ref:`~PyQt6.QtQuick.QQuickView.Status.Error`. The errors are available via :sip:ref:`~PyQt6.QtQuick.QQuickView.errors`.

:sip:ref:`~PyQt6.QtQuick.QQuickView` also manages sizing of the view and root object. By default, the :sip:ref:`~PyQt6.QtQuick.QQuickView.resizeMode` is :sip:ref:`~PyQt6.QtQuick.QQuickView.ResizeMode.SizeViewToRootObject`, which will load the component and resize it to the size of the view. Alternatively the :sip:ref:`~PyQt6.QtQuick.QQuickView.resizeMode` may be set to :sip:ref:`~PyQt6.QtQuick.QQuickView.ResizeMode.SizeRootObjectToView` which will resize the view to the size of the root object.

.. seealso:: `Exposing Attributes of C++ Types to QML <https://doc.qt.io/qt-6/qtqml-cppintegration-exposecppattributes.html>`_, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`.

.. sip:class-description::
    :status: todo
    :brief: Interface for asynchronous image loading in QQuickAsyncImageProvider
    :digest: 6a9e840475a9466ab5aad77e41966e6a

The :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse` class provides an interface for asynchronous image loading in :sip:ref:`~PyQt6.QtQuick.QQuickAsyncImageProvider`.

The purpose of an image response is to provide a way for image provider jobs to be executed in an asynchronous way.

Responses are deleted via deleteLater once the :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse.finished` signal has been emitted. If you are using :sip:ref:`~PyQt6.QtCore.QRunnable` as base for your :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse` ensure automatic deletion is disabled.

See the `Image Response Provider Example <https://doc.qt.io/qt-6/qtquick-imageresponseprovider-example.html>`_ for a complete implementation.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider`.

.. sip:class-description::
    :status: todo
    :brief: Helper class for selecting correct surface format
    :digest: 6aad7510db3ff92740a6ac85647d011c

Helper class for selecting correct surface format.

When using Qt Quick 3D with OpenGL it is necessary to take extra steps to define what kind of :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` is used when initializing Qt Quick. This is because by the time Qt Quick is aware that 3D content is being used, the OpenGL context and window surface has already been initialized. So this helper class is provided to request the ideal surface format from Qt Quick 3D so that it can be set as the default surface for Qt Quick before initialization.

If this helper is run when using any other rendering backends than OpenGL then it just returns a copy of the current default :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` with the requested samples.

If this helper is run when using the OpenGL rendering backend, then it will test for sufficiently modern versions of OpenGL and support for multisampling if requested. Normally Qt Quick will request an OpenGL 2.0 or OpenGL ES 2.0 context, which would limit the features available when using Qt Quick 3D, so an extra step is needed to request a more capable context.

The correct usage pattern is to call :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` to set the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` returned by QQuick3D::idealSurfaceFormat. It is important that this method is called after :sip:ref:`~PyQt6.QtGui.QGuiApplication` is constructed, but before the Qt Quick application content is loaded. This code snippet shows the correct usage pattern:

::

    #include <QGuiApplication>
    #include <QQmlApplicationEngine>

    #include <QtGui>
    #include <QtQuick3D/qquick3d.h>

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);

        QSurfaceFormat::setDefaultFormat(QQuick3D::idealSurfaceFormat(4));

        QQmlApplicationEngine engine;
        engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
        if (engine.rootObjects().isEmpty())
            return -1;

        return app.exec();
    }

.. seealso:: `OpenGL specifics <https://doc.qt.io/qt-6/qtquick3d-requirements.html>`_.

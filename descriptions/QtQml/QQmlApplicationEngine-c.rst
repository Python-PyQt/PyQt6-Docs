.. sip:class-description::
    :status: todo
    :brief: Convenient way to load an application from a single QML file
    :digest: 5cf4ea43f133e5e357772389cb9be51e

:sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine` provides a convenient way to load an application from a single QML file.

This class combines a :sip:ref:`~PyQt6.QtQml.QQmlEngine` and :sip:ref:`~PyQt6.QtQml.QQmlComponent` to provide a convenient way to load a single QML file. It also exposes some central application functionality to QML, which a C++/QML hybrid application would normally control from C++.

It can be used like so:

::

    #include <QGuiApplication>
    #include <QQmlApplicationEngine>

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        QQmlApplicationEngine engine("main.qml");
        return app.exec();
    }

Unlike :sip:ref:`~PyQt6.QtQuick.QQuickView`, :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine` does not automatically create a root window. If you are using visual items from Qt Quick, you will need to place them inside of a `Window <https://doc.qt.io/qt-6/qml-window.html>`_.

You can also use :sip:ref:`~PyQt6.QtCore.QCoreApplication` with :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine`, if you are not using any QML modules which require a :sip:ref:`~PyQt6.QtGui.QGuiApplication` (such as ``QtQuick``).

List of configuration changes from a default :sip:ref:`~PyQt6.QtQml.QQmlEngine`:

* Connecting Qt.quit() to :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`

* Automatically loads translation files from an i18n directory adjacent to the main QML file.

  * Translation files must have "qml_" prefix e.g. qml_ja_JP.qm.

* Translations are reloaded when the ``QJSEngine::uiLanguage`` / ``Qt.uiLanguage`` property is changed.

* Automatically sets an incubation controller if the scene contains a :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

* Automatically sets a ``QQmlFileSelector`` as the url interceptor, applying file selectors to all QML files and assets.

The engine behavior can be further tweaked by using the inherited methods from :sip:ref:`~PyQt6.QtQml.QQmlEngine`.

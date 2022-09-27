.. sip:class-description::
    :status: todo
    :brief: Abstract base for custom QML extension plugins
    :digest: 3a64a8c246c7a20b9f695d44671463d8

The :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` class provides an abstract base for custom QML extension plugins.

:sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` is a plugin interface that lets you create QML extensions that can be loaded dynamically into QML applications. These extensions allow custom QML types to be made available to the QML engine.

To write a QML extension plugin:

#. Subclass :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` and use the Q_PLUGIN_METADATA() macro to register the plugin with the Qt meta object system.

#. Use the QML_ELEMENT and QML_NAMED_ELEMENT() macros to declare QML types.

#. Configure your build file.

   CMake:

   ::

       qt_add_qml_module(<target>
           URI <my.import.name>
           VERSION 1.0
           QML_FILES <app.qml>
           NO_RESOURCE_TARGET_PATH
       )

   qmake:

   ::

       CONFIG += qmltypes
       QML_IMPORT_NAME = <my.import.name>
       QML_IMPORT_MAJOR_VERSION = <version>

#. If you're using qmake, create a `qmldir file <https://doc.qt.io/qt-6/qtqml-modules-qmldir.html>`_ to describe the plugin. Note that CMake will, by default, automatically generate the `qmldir file <https://doc.qt.io/qt-6/qtqml-modules-qmldir.html>`_.

QML extension plugins are for either application-specific or library-like plugins. Library plugins should limit themselves to registering types, as any manipulation of the engine's root context may cause conflicts or other issues in the library user's code.

The linker might erroneously remove the generated type registration function as an optimization. You can prevent that by declaring a synthetic volatile pointer to the function somewhere in your code. If your module is called "my.module", you would add the forward declaration in global scope:

::

    void qml_register_types_my_module();

Then add the following snippet of code in the implementation of any function that's part of the same binary as the registration:

::

    volatile auto registration = &qml_register_types_my_module;
    Q_UNUSED(registration);

.. _qqmlengineextensionplugin-timeexample-qml-extension-plugin:

TimeExample QML Extension Plugin
--------------------------------

Suppose there is a new ``TimeModel`` C++ class that should be made available as a new QML type. It provides the current time through ``hour`` and ``minute`` properties. It declares a QML type called ``Time`` via QML_NAMED_ELEMENT().

.. literalinclude:: ../../../snippets/qtdeclarative-examples-qml-qmlextensionplugins-timemodel.py

To make this type available, create a plugin class named ``QExampleQmlPlugin``, which is a subclass of :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin`. It uses the Q_PLUGIN_METADATA() macro in the class definition to register the plugin with the Qt meta object system using a unique identifier for the plugin.

.. literalinclude:: ../../../snippets/qtdeclarative-examples-qml-qmlextensionplugins-plugin.py

.. _qqmlengineextensionplugin-build-settings-for-the-plugin:

Build Settings for the Plugin
-----------------------------

The build file defines the project as a plugin library, specifies it should be built into the ``imports/TimeExample`` directory, and registers the plugin target name.

.. _qqmlengineextensionplugin-using-cmake:

Using CMake:
............

.. literalinclude:: ../../../snippets/qtdeclarative-examples-qml-qmlextensionplugins-CMakeLists.txt

.. literalinclude:: ../../../snippets/qtdeclarative-examples-qml-qmlextensionplugins-CMakeLists.txt

.. _qqmlengineextensionplugin-using-qmake:

Using qmake:
............

::

    TEMPLATE = lib
    CONFIG += qt plugin qmltypes
    QT += qml

    QML_IMPORT_NAME = TimeExample
    QML_IMPORT_MAJOR_VERSION = 1

    DESTDIR = imports/$$QML_IMPORT_NAME
    TARGET  = qmlqtimeexampleplugin

    SOURCES += qexampleqmlplugin.cpp

This registers the ``TimeModel`` class, with the import ``TimeExample 1.0``, as a QML type called ``Time``. The `Defining QML Types from C++ <https://doc.qt.io/qt-6/qtqml-cppintegration-definetypes.html>`_ article has more information about registering C++ types for usage in QML.

.. _qqmlengineextensionplugin-plugin-definition-in-the-qmldir:

Plugin Definition in the qmldir
-------------------------------

Finally, a `qmldir file <https://doc.qt.io/qt-6/qtqml-modules-qmldir.html>`_ is required in the ``imports/TimeExample`` directory to describe the plugin and the types that it exports. The plugin includes a ``Clock.qml`` file along with the ``qmlqtimeexampleplugin`` that is built by the project.

CMake will, by default, automatically generate this file. For more information, see `Auto-generating qmldir and typeinfo files <https://doc.qt.io/qt-6/qt-add-qml-module.html#auto-generating-qmldir-and-typeinfo-files>`_.

When using qmake, specify the following in the ``qmldir`` file:

To make things easier for this example, the TimeExample source directory is in ``imports/TimeExample``, and we build in-source. However, the structure of the source directory is not important, as the ``qmldir`` file can specify paths to installed QML files.

What is important is the name of the directory that the qmldir is installed into. When the user imports our module, the QML engine uses the `module identifier <https://doc.qt.io/qt-6/qtqml-modules-qmldir.html#contents-of-a-module-definition-qmldir-file>`_ (``TimeExample``) to find the plugin, so the directory in which it is installed must match the module identifier.

Once the project is built and installed, the new ``Time`` component is accessible by any QML component that imports the ``TimeExample`` module.

.. literalinclude:: ../../../snippets/qtdeclarative-examples-qml-qmlextensionplugins-plugins.qml

The full source code is available in the `plugins example <https://doc.qt.io/qt-6/qtqml-qmlextensionplugins-example.html>`_.

The `Writing QML Extensions with C++ <https://doc.qt.io/qt-6/qtqml-tutorials-extending-qml-example.html>`_ tutorial also contains a chapter on creating QML plugins.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.importPlugin`.

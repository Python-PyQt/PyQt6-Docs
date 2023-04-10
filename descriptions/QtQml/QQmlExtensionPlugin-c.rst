.. sip:class-description::
    :status: todo
    :brief: Abstract base for custom QML extension plugins with custom type registration functions
    :digest: 6f2bc90b5a153b333eb7ac1d1f658254

The :sip:ref:`~PyQt6.QtQml.QQmlExtensionPlugin` class provides an abstract base for custom QML extension plugins with custom type registration functions.

**Note:** If you need to write a plugin manually (which is rare) you should always use :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin`. :sip:ref:`~PyQt6.QtQml.QQmlExtensionPlugin` only provides the :sip:ref:`~PyQt6.QtQml.QQmlExtensionPlugin.registerTypes` and :sip:ref:`~PyQt6.QtQml.QQmlExtensionPlugin.unregisterTypes` functions in addition. You should not use them, but rather declare your types with QML_ELEMENT and friends and have the build system take care of the registration.

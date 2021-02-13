.. sip:method-description::
    :status: todo
    :pysig: 93190e040ea31e9fdc70db8c2bb40927
    :realsig: (QObject*)
    :digest: e2a6778978d54d772bf6a5d72b02cc70

Creates a JavaScript object that wraps the given :sip:ref:`~PyQt6.QtCore.QObject` *object*, using :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership.JavaScriptOwnership`.

Signals and slots, properties and children of *object* are available as properties of the created :sip:ref:`~PyQt6.QtQml.QJSValue`.

If *object* is a null pointer, this function returns a null value.

If a default prototype has been registered for the *object*'s class (or its superclass, recursively), the prototype of the new script object will be set to be that default prototype.

If the given *object* is deleted outside of the engine's control, any attempt to access the deleted :sip:ref:`~PyQt6.QtCore.QObject`'s members through the JavaScript wrapper object (either by script code or C++) will result in a :ref:`qjsengine-script-exceptions`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.toQObject`.

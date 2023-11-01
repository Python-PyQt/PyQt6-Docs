.. sip:method-description::
    :status: todo
    :pysig: e8d0aa8a6c2e6e9d30fda8a46f68efeb
    :realsig: (const QString&, const QJSValue&)
    :digest: d54912fd8e0839bfafb8788a38260e4d

Registers a :sip:ref:`~PyQt6.QtQml.QJSValue` to serve as a module. After this function is called, all modules that import *moduleName* will import the value of *value* instead of loading *moduleName* from the filesystem.

Any valid :sip:ref:`~PyQt6.QtQml.QJSValue` can be registered, but named exports (i.e. ``import { name } from "info"`` are treated as members of an object, so the default export must be created with one of the newXYZ methods of :sip:ref:`~PyQt6.QtQml.QJSEngine`.

Because this allows modules that do not exist on the filesystem to be imported, scripting applications can use this to provide built-in modules, similar to Node.js.

Returns ``true`` on success, ``false`` otherwise.

**Note:** The :sip:ref:`~PyQt6.QtQml.QJSValue` *value* is not called or read until it is used by another module. This means that there is no code to evaluate, so no errors will be seen until another module throws an exception while trying to load this module.

**Warning:** Attempting to access a named export from a :sip:ref:`~PyQt6.QtQml.QJSValue` that is not an object will trigger a :ref:`qjsengine-script-exceptions`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.importModule`.

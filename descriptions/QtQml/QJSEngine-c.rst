.. sip:class-description::
    :status: todo
    :brief: Environment for evaluating JavaScript code
    :digest: 2005cd00491fed6512c262ea67ebafc4

The :sip:ref:`~PyQt6.QtQml.QJSEngine` class provides an environment for evaluating JavaScript code.

.. _qjsengine-evaluating-scripts:

Evaluating Scripts
------------------

Use :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` to evaluate script code.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 54-55

:sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` returns a :sip:ref:`~PyQt6.QtQml.QJSValue` that holds the result of the evaluation. The :sip:ref:`~PyQt6.QtQml.QJSValue` class provides functions for converting the result to various C++ types (e.g. QJSValue::toString() and QJSValue::toNumber()).

The following code snippet shows how a script function can be defined and then invoked from C++ using QJSValue::call():

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 60-63

As can be seen from the above snippets, a script is provided to the engine in the form of a string. One common way of loading scripts is by reading the contents of a file and passing it to :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate`:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 68-75

Here we pass the name of the file as the second argument to :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate`. This does not affect evaluation in any way; the second argument is a general-purpose string that is stored in the ``Error`` object for debugging purposes.

For larger pieces of functionality, you may want to encapsulate your code and data into modules. A module is a file that contains script code, variables, etc., and uses export statements to describe its interface towards the rest of the application. With the help of import statements, a module can refer to functionality from other modules. This allows building a scripted application from smaller connected building blocks in a safe way. In contrast, the approach of using :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` carries the risk that internal variables or functions from one :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` call accidentally pollute the global object and affect subsequent evaluations.

The following example provides a module that can add numbers:

::

    export function sum(left, right)
    {
        return left + right
    }

This module can be loaded with QJSEngine::import() if it is saved under the name ``math.mjs``:

::

    QJSvalue module = myEngine.importModule("./math.mjs");
    QJSValue sumFunction = module.property("sum");
    QJSValue result = sumFunction.call(args);

Modules can also use functionality from other modules using import statements:

::

    import { sum } from "./math.mjs";
    export function addTwice(left, right)
    {
        return sum(left, right) * 2;
    }

Modules don't have to be files. They can be values registered with :sip:ref:`~PyQt6.QtQml.QJSEngine.registerModule`:

::

    import version from "version";

    export function getVersion()
    {
        return version;
    }

::

    QJSValue version(610);
    myEngine.registerModule("version", version);
    QJSValue module = myEngine.importModule("./myprint.mjs");
    QJSValue getVersion = module.property("getVersion");
    QJSValue result = getVersion.call();

Named exports are supported, but because they are treated as members of an object, the default export must be an ECMAScript object. Most of the newXYZ functions in :sip:ref:`~PyQt6.QtQml.QJSValue` will return an object.

::

    QJSValue name("Qt6");
    QJSValue obj = myEngine.newObject();
    obj.setProperty("name", name);
    myEngine.registerModule("info", obj);

::

    import { name } from "info";

    export function getName()
    {
        return name;
    }

.. _qjsengine-engine-configuration:

Engine Configuration
--------------------

The :sip:ref:`~PyQt6.QtQml.QJSEngine.globalObject` function returns the **Global Object** associated with the script engine. Properties of the Global Object are accessible from any script code (i.e. they are global variables). Typically, before evaluating "user" scripts, you will want to configure a script engine by adding one or more properties to the Global Object:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 80-82

Adding custom properties to the scripting environment is one of the standard means of providing a scripting API that is specific to your application. Usually these custom properties are objects created by the :sip:ref:`~PyQt6.QtQml.QJSEngine.newQObject` or :sip:ref:`~PyQt6.QtQml.QJSEngine.newObject` functions.

.. _qjsengine-script-exceptions:

Script Exceptions
-----------------

:sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` can throw a script exception (e.g. due to a syntax error). If it does, then :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` returns the value that was thrown (typically an ``Error`` object). Use QJSValue::isError() to check for exceptions.

For detailed information about the error, use QJSValue::toString() to obtain an error message, and use QJSValue::property() to query the properties of the ``Error`` object. The following properties are available:

* ``name``

* ``message``

* ``fileName``

* ``lineNumber``

* ``stack``

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 87-92

.. _qjsengine-script-object-creation:

Script Object Creation
----------------------

Use :sip:ref:`~PyQt6.QtQml.QJSEngine.newObject` to create a JavaScript object; this is the C++ equivalent of the script statement ``new Object()``. You can use the object-specific functionality in :sip:ref:`~PyQt6.QtQml.QJSValue` to manipulate the script object (e.g. QJSValue::setProperty()). Similarly, use :sip:ref:`~PyQt6.QtQml.QJSEngine.newArray` to create a JavaScript array object.

.. _qjsengine-qobject-integration:

QObject Integration
-------------------

Use :sip:ref:`~PyQt6.QtQml.QJSEngine.newQObject` to wrap a :sip:ref:`~PyQt6.QtCore.QObject` (or subclass) pointer. :sip:ref:`~PyQt6.QtQml.QJSEngine.newQObject` returns a proxy script object; properties, children, and signals and slots of the :sip:ref:`~PyQt6.QtCore.QObject` are available as properties of the proxy object. No binding code is needed because it is done dynamically using the Qt meta object system.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 97-104

Use :sip:ref:`~PyQt6.QtQml.QJSEngine.newQMetaObject` to wrap a :sip:ref:`~PyQt6.QtCore.QMetaObject`; this gives you a "script representation" of a :sip:ref:`~PyQt6.QtCore.QObject`-based class. :sip:ref:`~PyQt6.QtQml.QJSEngine.newQMetaObject` returns a proxy script object; enum values of the class are available as properties of the proxy object.

Constructors exposed to the meta-object system (using Q_INVOKABLE) can be called from the script to create a new :sip:ref:`~PyQt6.QtCore.QObject` instance with :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership.JavaScriptOwnership`. For example, given the following class definition:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 122-128

The ``staticMetaObject`` for the class can be exposed to JavaScript like so:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 132-133

Instances of the class can then be created in JavaScript:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 137-137

**Note:** Currently only classes using the Q_OBJECT macro are supported; it is not possible to expose the ``staticMetaObject`` of a Q_GADGET class to JavaScript.

.. _qjsengine-dynamic-qobject-properties:

Dynamic QObject Properties
..........................

Dynamic :sip:ref:`~PyQt6.QtCore.QObject` properties are not supported. For example, the following code will not work:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsengine.py
    :lines: 109-117

.. _qjsengine-extensions:

Extensions
----------

:sip:ref:`~PyQt6.QtQml.QJSEngine` provides a compliant ECMAScript implementation. By default, familiar utilities like logging are not available, but they can can be installed via the :sip:ref:`~PyQt6.QtQml.QJSEngine.installExtensions` function.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue`, `Making Applications Scriptable <https://doc.qt.io/qt-6/qtjavascript.html>`_, `List of JavaScript Objects and Functions <https://doc.qt.io/qt-6/qtqml-javascript-functionlist.html>`_.

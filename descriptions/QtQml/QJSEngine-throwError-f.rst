.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 3462bd24e738a140c2f26a15f84379cc

Throws a run-time error (exception) with the given *message*.

This method is the C++ counterpart of a ``throw()`` expression in JavaScript. It enables C++ code to report run-time errors to :sip:ref:`~PyQt6.QtQml.QJSEngine`. Therefore it should only be called from C++ code that was invoked by a JavaScript function through :sip:ref:`~PyQt6.QtQml.QJSEngine`.

When returning from C++, the engine will interrupt the normal flow of execution and call the the next pre-registered exception handler with an error object that contains the given *message*. The error object will point to the location of the top-most context on the JavaScript caller stack; specifically, it will have properties ``lineNumber``, ``fileName`` and ``stack``. These properties are described in :ref:`qjsengine-script-exceptions`.

In the following example a C++ method in *FileAccess.cpp* throws an error in *qmlFile.qml* at the position where ``readFileAsText()`` is called:

::

    // qmlFile.qml
    function someFunction() {
      ...
      var text = FileAccess.readFileAsText("/path/to/file.txt");
    }

::

    // FileAccess.cpp
    // Assuming that FileAccess is a QObject-derived class that has been
    // registered as a singleton type and provides an invokable method
    // readFileAsText()

    QJSValue FileAccess::readFileAsText(const QString & filePath) {
      QFile file(filePath);

      if (!file.open(QIODevice::ReadOnly)) {
        jsEngine->throwError(file.errorString());
        return QString();
      }

      ...
      return content;
    }

It is also possible to catch the thrown error in JavaScript:

::

    // qmlFile.qml
    function someFunction() {
      ...
      var text;
      try {
        text = FileAccess.readFileAsText("/path/to/file.txt");
      } catch (error) {
        console.warn("In " + error.fileName + ":" + "error.lineNumber" +
                     ": " + error.message);
      }
    }

If you need a more specific run-time error to describe an exception, you can use the throwError(QJSValue::ErrorType errorType, const QString &message) overload.

.. seealso:: :ref:`qjsengine-script-exceptions`.

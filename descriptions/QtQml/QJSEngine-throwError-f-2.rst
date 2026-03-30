.. sip:method-description::
    :status: todo
    :pysig: 4536ae4cca00947a81b63d0c4b0c5c4f
    :realsig: (QJSValue::ErrorType, const QString&)
    :digest: 4620a35dca2f9bb9cf8fcb356e342c8a

Throws a run-time error (exception) with the given *errorType* and *message*.

::

    // Assuming that DataEntry is a QObject-derived class that has been
    // registered as a singleton type and provides an invokable method
    // setAge().

    void DataEntry::setAge(int age) {
      if (age < 0 || age > 200) {
        jsEngine->throwError(QJSValue::RangeError,
                             "Age must be between 0 and 200");
      }
      ...
    }

.. seealso:: :ref:`qjsengine-script-exceptions`, :sip:ref:`~PyQt6.QtQml.QJSEngine.newErrorObject`.

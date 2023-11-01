.. sip:method-description::
    :status: todo
    :pysig: e33ab3882276d8678e53773f862e3196
    :realsig: (QJSValue::ErrorType, const QString&)
    :digest: 7e5f901d1b5a08792a0c90d1a09f0b7e

This function overloads :sip:ref:`~PyQt6.QtQml.QJSEngine.throwError`.

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

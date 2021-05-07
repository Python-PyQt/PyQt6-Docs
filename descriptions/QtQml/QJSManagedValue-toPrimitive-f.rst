.. sip:method-description::
    :status: todo
    :pysig: 9897c86a8be780e69ea5827d1c06babb
    :realsig: () const
    :digest: 8342d1ad9b9a340455823910c70e324d

Converts the manged value to a :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`. If the managed value holds a type supported by :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`, the value is copied. Otherwise the value is converted to a string, and the string is stored in :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`.

**Note:** Conversion of a managed value to a string can throw an exception. In particular, symbols cannot be coerced into strings, or a custom :sip:ref:`~PyQt6.QtQml.QJSManagedValue.toString` method may throw. In this case the result is the undefined value and the engine carries an error after the conversion.

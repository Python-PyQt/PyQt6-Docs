.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 3e3ca086950d1d724fe26b448f00f9c0

Converts the manged value to a string. If the managed value holds a string, that one is returned. Otherwise a string coercion by JavaScript rules is performed.

**Note:** Conversion of a managed value to a string can throw an exception. In particular, symbols cannot be coerced into strings, or a custom  method may throw. In this case the result is an empty string and the engine carries an error after the conversion.

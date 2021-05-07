.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 19496faf835385ab846357e5ea776de5

Converts the manged value to a number. If the managed value holds a number, that one is returned. Otherwise a number coercion by JavaScript rules is performed.

**Note:** Conversion of a managed value to a number can throw an exception. In particular, symbols cannot be coerced into numbers, or a custom valueOf() method may throw. In this case the result is 0 and the engine carries an error after the conversion.

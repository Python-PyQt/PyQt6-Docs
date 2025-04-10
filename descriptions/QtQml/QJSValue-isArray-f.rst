.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9eb409dfac4c6da66ecfcb7454a2f583

Returns true if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object of the Array class; otherwise returns false.

**Note:** This method is the equivalent of *Array.isArray()* in JavaScript. You can use it to identify JavaScript arrays, but it will return ``false`` for any array-like objects that are not JavaScript arrays. This includes QML *list* objects for either value types or object types, JavaScript typed arrays, JavaScript ArrayBuffer objects, and any custom array-like objects you may create yourself. All of these *behave* like JavaScript arrays, though: They generally expose the same methods and the subscript operator can be used on them. Therefore, using this method to determine whether an object could be used like an array is not advisable.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.newArray`.

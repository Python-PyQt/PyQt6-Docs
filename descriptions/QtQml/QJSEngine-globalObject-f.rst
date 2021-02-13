.. sip:method-description::
    :status: todo
    :pysig: 916cc5874b398a0d71e2a98c93e7db3e
    :realsig: () const
    :digest: 82e75893c2a2fe8559328c7d80e534b4

Returns this engine's Global Object.

By default, the Global Object contains the built-in objects that are part of `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_, such as Math, Date and String. Additionally, you can set properties of the Global Object to make your own extensions available to all script code. Non-local variables in script code will be created as properties of the Global Object, as well as local variables in global code.

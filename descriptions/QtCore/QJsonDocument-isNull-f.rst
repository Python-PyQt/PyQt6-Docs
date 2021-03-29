.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ec0a46aca76df3358c16b1ed328c8efd

returns ``true`` if this document is null.

Null documents are documents created through the default constructor.

Documents created from UTF-8 encoded text or the binary format are validated during parsing. If validation fails, the returned document will also be null.

.. sip:method-description::
    :status: todo
    :pysig: b72a54a27b522c26039a59b2a7e68654
    :realsig: (const QString&, bool, QString*, int*, int*)
    :digest: 55aae682caf5707922c36b7d09584c27

Use the overloads taking ParseOptions instead.

This function reads the XML document from the string *text*, returning true if the content was successfully parsed; otherwise returns ``false``. Since *text* is already a Unicode string, no encoding detection is done.

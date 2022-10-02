.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a8ef00ac87d1529a6f7cfdabe33912c4

Commits the word user is currently composing to the editor. The function is mostly needed by the input methods with text prediction features and by the methods where the script used for typing characters is different from the script that actually gets appended to the editor. Any kind of action that interrupts the text composing needs to flush the composing state by calling the commit() function, for example when the cursor is moved elsewhere.

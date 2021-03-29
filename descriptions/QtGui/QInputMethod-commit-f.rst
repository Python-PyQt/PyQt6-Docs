.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fbbdfd064d0e7c4fc6823f969bdb6221

Commits the word user is currently composing to the editor. The function is mostly needed by the input methods with text prediction features and by the methods where the script used for typing characters is different from the script that actually gets appended to the editor. Any kind of action that interrupts the text composing needs to flush the composing state by calling the  function, for example when the cursor is moved elsewhere.

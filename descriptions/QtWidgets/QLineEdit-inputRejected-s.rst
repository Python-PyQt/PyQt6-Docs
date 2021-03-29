.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: bcc733222936580a83603ffa87adaee8

This signal is emitted when the user presses a key that is not considered to be acceptable input. For example, if a key press results in a validator's validate() call to return Invalid. Another case is when trying to enter in more characters beyond the maximum length of the line edit.

Note: This signal will still be emitted in a case where part of the text is accepted but not all of it is. For example, if there is a maximum length set and the clipboard text is longer than the maximum length when it is pasted.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 341608b8fd1f29f6a92f193a7ea9d575

Reset the internal state of the view.

**Warning:** This function will reset open editors, scroll bar positions, selections, etc. Existing changes will not be committed. If you would like to save your changes when resetting the view, you can reimplement this function, commit your changes, and then call the superclass' implementation.

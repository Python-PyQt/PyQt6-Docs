.. sip:method-description::
    :status: todo
    :pysig: 529d3d63ad7379453499ed1a2fddbbc9
    :realsig: (QPoint*)
    :digest: 4003da3341547028675e41936ce968d7

Reimplemented in subclasses to return the real window this render control is rendering into.

If *offset* in non-null, it is set to the offset of the control inside the window.

**Note:** While not mandatory, reimplementing this function becomes essential for supporting multiple screens with different device pixel ratios and properly positioning popup windows opened from QML. Therefore providing it in subclasses is highly recommended.

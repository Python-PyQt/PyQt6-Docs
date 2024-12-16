.. sip:method-description::
    :status: todo
    :pysig: 6ba43ab6ef3b48e6b51ab951b4123cee
    :realsig: (QAnyStringView)
    :digest: 9b411c40959c897245e3f3217ee0ee27

Returns the frame with the given *name*. If there are multiple frames with the same name, which one is returned is arbitrary. If no frame was found, returns ``std::nullopt``.

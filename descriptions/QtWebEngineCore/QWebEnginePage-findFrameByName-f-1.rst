.. sip:method-description::
    :status: todo
    :pysig: d343ec2831c58344b95453f79fd93efe
    :realsig: (QAnyStringView)
    :digest: 9b411c40959c897245e3f3217ee0ee27

Returns the frame with the given *name*. If there are multiple frames with the same name, which one is returned is arbitrary. If no frame was found, returns ``std::nullopt``.

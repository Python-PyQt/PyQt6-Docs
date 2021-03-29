.. sip:method-description::
    :status: todo
    :pysig: 85614b66e1780877cf0b12760bffaa85
    :realsig: (const QUrl&) const
    :digest: 0da8578fb7fa11f01bc7ee4e28bd28f9

Returns the corrected URL for the *url* that may refer to a different namespace defined by the virtual folder defined as a part of the *url*. If the virtual folder matches the namespace of the *url*, the method just checks if the file exists and returns the same *url*. When the virtual folder doesn't match the namespace of the *url*, it tries to find the best matching namespace according to the active filter. When the namespace is found, it returns the corrected URL if the file exists, otherwise it returns an invalid URL.

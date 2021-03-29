.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 403ecb8b52cf4ce1e0e6a61dd046c5a9

Reads until the end of the current element, skipping any child nodes. This function is useful for skipping unknown elements.

The current element is the element matching the most recently parsed start element of which a matching end element has not yet been reached. When the parser has reached the end element, the current element becomes the parent element.

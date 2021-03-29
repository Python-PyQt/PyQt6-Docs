.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2d677ad4ccfb8e1814a083656f32f557

Returns ``true`` if writing failed.

This can happen if the stream failed to write to the underlying device or if the data to be written contained invalid characters.

The error status is never reset. Writes happening after the error occurred may be ignored, even if the error condition is cleared.

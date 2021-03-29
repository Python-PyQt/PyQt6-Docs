.. sip:method-description::
    :status: todo
    :pysig: 5b478d7b6732b1ed04b555693a2b6e95
    :realsig: (const QOpenGLVersionProfile&,QOpenGLContext*)
    :digest: 2454d0c6da067e262cf93ddd2c604022

Returns a pointer to an object that provides access to all functions for the *versionProfile* of the *context*. There is no need to call  as long as the *context* is current. It is also possible to call this function when the *context* is not current, but in that case it is the caller's responsibility to ensure proper initialization by calling  afterwards.

Usually one would use the template version of this function to automatically have the result cast to the correct type.

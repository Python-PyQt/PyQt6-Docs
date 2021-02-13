.. sip:method-description::
    :status: todo
    :pysig: 49c4e82b5e484f0f98053794b701c0e7
    :realsig: () const
    :digest: 40ffbfb70e648aa2dd4ef56b66e2e4a7

Returns a pointer to the native certificate handle, if there is one, else ``nullptr``.

You can use this handle, together with the native API, to access extended information about the certificate.

**Warning:** Use of this function has a high probability of being non-portable, and its return value may vary from platform to platform or change from minor release to minor release.

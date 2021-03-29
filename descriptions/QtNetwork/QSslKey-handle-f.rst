.. sip:method-description::
    :status: todo
    :pysig: 49c4e82b5e484f0f98053794b701c0e7
    :realsig: () const
    :digest: 08a3eb15a8c5ed38fcb32ff32edb3b05

Returns a pointer to the native key handle, if there is one, else ``nullptr``.

You can use this handle together with the native API to access extended information about the key.

**Warning:** Use of this function has a high probability of being non-portable, and its return value may vary across platforms, and between minor Qt releases.

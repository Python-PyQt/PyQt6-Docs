.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b796b51e62e7a0c3d3f4c5180c3bc41e

Disconnects and destroys the COM object.

If you reimplement this function you must also reimplement the destructor to call clear(), and call this implementation at the end of your clear() function.

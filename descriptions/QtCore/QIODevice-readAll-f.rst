.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: ()
    :digest: eaba8924d663d2c2c0dd40ede2a3f031

Reads all remaining data from the device, and returns it as a byte array.

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for reading, or that an error occurred.

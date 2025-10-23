.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b5810f6fe8be1b7b8961a5a06f3c776e

Returns the database-specific (native) error code, or an empty string if it cannot be determined.

**Note:** Some drivers (like DB2 or ODBC) may return more than one error code. When this happens, ``;`` is used as separator between the error codes.

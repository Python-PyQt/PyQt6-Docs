.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 6381e6e7a047a27f23bc09de23f20bbb

Returns the database-specific error code, or an empty string if it cannot be determined.

**Note:** Some drivers (like DB2 or ODBC) may return more than one error code. When this happens, ``;`` is used as separator between the error codes.

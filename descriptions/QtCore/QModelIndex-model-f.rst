.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: () const
    :digest: 0dc9db8f2de278e87f00a6c18a933cdd

Returns a pointer to the model containing the item that this index refers to.

A const pointer to the model is returned because calls to non-const functions of the model might invalidate the model index and possibly crash your application.

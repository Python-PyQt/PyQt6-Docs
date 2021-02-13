.. sip:method-description::
    :status: todo
    :pysig: 1794526a133c101ed5249f3aa1e3bdff
    :realsig: (int,QObject*)
    :digest: cbf8449b5ba072dae358ae98d0ee899e

Registers the given *component* as a handler for items of the given *objectType*.

**Note:**  has to be called once for each object type. This means that there is only one handler for multiple replacement characters of the same object type.

The text document layout does not take ownership of ``component``.

.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 6889b1ede34cac1c05246b20a2531fd4

This signal is emitted whenever the content of the document changes in a way that affects the modification state. If *changed* is true, the document has been modified; otherwise it is false.

For example, calling setModified(false) on a document and then inserting text causes the signal to get emitted. If you undo that operation, causing the document to return to its original unmodified state, the signal will get emitted again.

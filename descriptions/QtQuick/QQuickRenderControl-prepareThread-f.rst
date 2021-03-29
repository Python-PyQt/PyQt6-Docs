.. sip:method-description::
    :status: todo
    :pysig: f66b8fe5c9a42a71784b0410e54eafff
    :realsig: (QThread*)
    :digest: cea0bbeeb6784d8b198662c5d9155a60

Prepares rendering the Qt Quick scene outside the GUI thread.

*targetThread* specifies the thread on which synchronization and rendering will happen. There is no need to call this function in a single threaded scenario.

.. sip:method-description::
    :status: todo
    :pysig: 4f0945bdf86581e51cc69bc1f473b905
    :realsig: (const QMimeData*) const
    :digest: 1db7a83a829fc9f4bc966228ee43570a

This function returns ``true`` if the contents of the MIME data object, specified by *source*, can be decoded and inserted into the document. It is called for example when during a drag operation the mouse enters this widget and it is necessary to determine whether it is possible to accept the drag and drop operation.

Reimplement this function to enable drag and drop support for additional MIME types.

.. sip:method-description::
    :status: todo
    :pysig: 4f0945bdf86581e51cc69bc1f473b905
    :realsig: (const QMimeData*) const
    :digest: 9cfbbad98f39e8c73ec0ecae95c95a4e

This function returns ``true`` if the contents of the MIME data object, specified by *source*, can be decoded and inserted into the document. It is called for example when during a drag operation the mouse enters this widget and it is necessary to determine whether it is possible to accept the drag.

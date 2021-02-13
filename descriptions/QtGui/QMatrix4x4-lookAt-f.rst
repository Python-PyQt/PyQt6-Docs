.. sip:method-description::
    :status: todo
    :pysig: 5f2ac4790b1e0502d2b5442b3b34d07f
    :realsig: (const QVector3D&,const QVector3D&,const QVector3D&)
    :digest: 87f9309dacf39ea8ffda8b0f408b7e7f

Multiplies this matrix by a viewing matrix derived from an eye point. The *center* value indicates the center of the view that the *eye* is looking at. The *up* value indicates which direction should be considered up with respect to the *eye*.

**Note:** The *up* vector must not be parallel to the line of sight from *eye* to *center*.

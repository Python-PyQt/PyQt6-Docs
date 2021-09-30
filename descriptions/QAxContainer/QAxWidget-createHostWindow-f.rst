.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: 362cb21705573779cc3c7b1937171193

Creates the client site for the ActiveX control, and returns true if the control could be embedded successfully, otherwise returns false. If *initialized* is true the control has already been initialized.

This function is called by initialize(). If you reimplement initialize to customize the actual control instantiation, call this function in your reimplementation to have the control embedded by the default client side. Creates the client site for the ActiveX control, and returns true if the control could be embedded successfully, otherwise returns false.

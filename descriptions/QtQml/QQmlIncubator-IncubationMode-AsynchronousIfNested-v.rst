.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: b0d7a8ec6340664801d085e7a5357972

If the object is being created in a context that is already part of an asynchronous creation, this incubator will join that existing incubation and execute asynchronously. The existing incubation will not become Ready until both it and this incubation have completed. Otherwise, the incubation will execute synchronously.

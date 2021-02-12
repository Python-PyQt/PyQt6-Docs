.. sip:enum-description::
    :status: todo
    :digest: a6408fa50c5cac08a0e7e918409d998a

Each item in the model has a set of data elements associated with it, each with its own role. The roles are used by the view to indicate to the model which type of data it needs. Custom models should return data in these types.

The general purpose roles (and the associated types) are:

Roles describing appearance and meta data (with associated types):

Accessibility roles (with associated types):

User roles:

For user roles, it is up to the developer to decide which types to use and ensure that components use the correct types when accessing and setting data.

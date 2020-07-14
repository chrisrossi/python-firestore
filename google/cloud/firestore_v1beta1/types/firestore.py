# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.firestore_v1beta1.types import common
from google.cloud.firestore_v1beta1.types import document as gf_document
from google.cloud.firestore_v1beta1.types import query as gf_query
from google.cloud.firestore_v1beta1.types import write
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.firestore.v1beta1",
    manifest={
        "GetDocumentRequest",
        "ListDocumentsRequest",
        "ListDocumentsResponse",
        "CreateDocumentRequest",
        "UpdateDocumentRequest",
        "DeleteDocumentRequest",
        "BatchGetDocumentsRequest",
        "BatchGetDocumentsResponse",
        "BeginTransactionRequest",
        "BeginTransactionResponse",
        "CommitRequest",
        "CommitResponse",
        "RollbackRequest",
        "RunQueryRequest",
        "RunQueryResponse",
        "WriteRequest",
        "WriteResponse",
        "ListenRequest",
        "ListenResponse",
        "Target",
        "TargetChange",
        "ListCollectionIdsRequest",
        "ListCollectionIdsResponse",
    },
)


class GetDocumentRequest(proto.Message):
    r"""The request for
    [Firestore.GetDocument][google.firestore.v1beta1.Firestore.GetDocument].

    Attributes:
        name (str):
            Required. The resource name of the Document to get. In the
            format:
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
        mask (~.common.DocumentMask):
            The fields to return. If not set, returns all
            fields.
            If the document has a field that is not present
            in this mask, that field will not be returned in
            the response.
        transaction (bytes):
            Reads the document in a transaction.
        read_time (~.timestamp.Timestamp):
            Reads the version of the document at the
            given time. This may not be older than 60
            seconds.
    """

    name = proto.Field(proto.STRING, number=1)

    mask = proto.Field(proto.MESSAGE, number=2, message=common.DocumentMask,)

    transaction = proto.Field(proto.BYTES, number=3, oneof="consistency_selector")

    read_time = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="consistency_selector",
        message=timestamp.Timestamp,
    )


class ListDocumentsRequest(proto.Message):
    r"""The request for
    [Firestore.ListDocuments][google.firestore.v1beta1.Firestore.ListDocuments].

    Attributes:
        parent (str):
            Required. The parent resource name. In the format:
            ``projects/{project_id}/databases/{database_id}/documents``
            or
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
            For example:
            ``projects/my-project/databases/my-database/documents`` or
            ``projects/my-project/databases/my-database/documents/chatrooms/my-chatroom``
        collection_id (str):
            Required. The collection ID, relative to ``parent``, to
            list. For example: ``chatrooms`` or ``messages``.
        page_size (int):
            The maximum number of documents to return.
        page_token (str):
            The ``next_page_token`` value returned from a previous List
            request, if any.
        order_by (str):
            The order to sort results by. For example:
            ``priority desc, name``.
        mask (~.common.DocumentMask):
            The fields to return. If not set, returns all
            fields.
            If a document has a field that is not present in
            this mask, that field will not be returned in
            the response.
        transaction (bytes):
            Reads documents in a transaction.
        read_time (~.timestamp.Timestamp):
            Reads documents as they were at the given
            time. This may not be older than 60 seconds.
        show_missing (bool):
            If the list should show missing documents. A missing
            document is a document that does not exist but has
            sub-documents. These documents will be returned with a key
            but will not have fields,
            [Document.create_time][google.firestore.v1beta1.Document.create_time],
            or
            [Document.update_time][google.firestore.v1beta1.Document.update_time]
            set.

            Requests with ``show_missing`` may not specify ``where`` or
            ``order_by``.
    """

    parent = proto.Field(proto.STRING, number=1)

    collection_id = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    order_by = proto.Field(proto.STRING, number=6)

    mask = proto.Field(proto.MESSAGE, number=7, message=common.DocumentMask,)

    transaction = proto.Field(proto.BYTES, number=8, oneof="consistency_selector")

    read_time = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="consistency_selector",
        message=timestamp.Timestamp,
    )

    show_missing = proto.Field(proto.BOOL, number=12)


class ListDocumentsResponse(proto.Message):
    r"""The response for
    [Firestore.ListDocuments][google.firestore.v1beta1.Firestore.ListDocuments].

    Attributes:
        documents (Sequence[~.gf_document.Document]):
            The Documents found.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    documents = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gf_document.Document,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class CreateDocumentRequest(proto.Message):
    r"""The request for
    [Firestore.CreateDocument][google.firestore.v1beta1.Firestore.CreateDocument].

    Attributes:
        parent (str):
            Required. The parent resource. For example:
            ``projects/{project_id}/databases/{database_id}/documents``
            or
            ``projects/{project_id}/databases/{database_id}/documents/chatrooms/{chatroom_id}``
        collection_id (str):
            Required. The collection ID, relative to ``parent``, to
            list. For example: ``chatrooms``.
        document_id (str):
            The client-assigned document ID to use for
            this document.
            Optional. If not specified, an ID will be
            assigned by the service.
        document (~.gf_document.Document):
            Required. The document to create. ``name`` must not be set.
        mask (~.common.DocumentMask):
            The fields to return. If not set, returns all
            fields.
            If the document has a field that is not present
            in this mask, that field will not be returned in
            the response.
    """

    parent = proto.Field(proto.STRING, number=1)

    collection_id = proto.Field(proto.STRING, number=2)

    document_id = proto.Field(proto.STRING, number=3)

    document = proto.Field(proto.MESSAGE, number=4, message=gf_document.Document,)

    mask = proto.Field(proto.MESSAGE, number=5, message=common.DocumentMask,)


class UpdateDocumentRequest(proto.Message):
    r"""The request for
    [Firestore.UpdateDocument][google.firestore.v1beta1.Firestore.UpdateDocument].

    Attributes:
        document (~.gf_document.Document):
            Required. The updated document.
            Creates the document if it does not already
            exist.
        update_mask (~.common.DocumentMask):
            The fields to update.
            None of the field paths in the mask may contain
            a reserved name.
            If the document exists on the server and has
            fields not referenced in the mask, they are left
            unchanged.
            Fields referenced in the mask, but not present
            in the input document, are deleted from the
            document on the server.
        mask (~.common.DocumentMask):
            The fields to return. If not set, returns all
            fields.
            If the document has a field that is not present
            in this mask, that field will not be returned in
            the response.
        current_document (~.common.Precondition):
            An optional precondition on the document.
            The request will fail if this is set and not met
            by the target document.
    """

    document = proto.Field(proto.MESSAGE, number=1, message=gf_document.Document,)

    update_mask = proto.Field(proto.MESSAGE, number=2, message=common.DocumentMask,)

    mask = proto.Field(proto.MESSAGE, number=3, message=common.DocumentMask,)

    current_document = proto.Field(
        proto.MESSAGE, number=4, message=common.Precondition,
    )


class DeleteDocumentRequest(proto.Message):
    r"""The request for
    [Firestore.DeleteDocument][google.firestore.v1beta1.Firestore.DeleteDocument].

    Attributes:
        name (str):
            Required. The resource name of the Document to delete. In
            the format:
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
        current_document (~.common.Precondition):
            An optional precondition on the document.
            The request will fail if this is set and not met
            by the target document.
    """

    name = proto.Field(proto.STRING, number=1)

    current_document = proto.Field(
        proto.MESSAGE, number=2, message=common.Precondition,
    )


class BatchGetDocumentsRequest(proto.Message):
    r"""The request for
    [Firestore.BatchGetDocuments][google.firestore.v1beta1.Firestore.BatchGetDocuments].

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``.
        documents (Sequence[str]):
            The names of the documents to retrieve. In the format:
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
            The request will fail if any of the document is not a child
            resource of the given ``database``. Duplicate names will be
            elided.
        mask (~.common.DocumentMask):
            The fields to return. If not set, returns all
            fields.
            If a document has a field that is not present in
            this mask, that field will not be returned in
            the response.
        transaction (bytes):
            Reads documents in a transaction.
        new_transaction (~.common.TransactionOptions):
            Starts a new transaction and reads the
            documents. Defaults to a read-only transaction.
            The new transaction ID will be returned as the
            first response in the stream.
        read_time (~.timestamp.Timestamp):
            Reads documents as they were at the given
            time. This may not be older than 60 seconds.
    """

    database = proto.Field(proto.STRING, number=1)

    documents = proto.RepeatedField(proto.STRING, number=2)

    mask = proto.Field(proto.MESSAGE, number=3, message=common.DocumentMask,)

    transaction = proto.Field(proto.BYTES, number=4, oneof="consistency_selector")

    new_transaction = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="consistency_selector",
        message=common.TransactionOptions,
    )

    read_time = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="consistency_selector",
        message=timestamp.Timestamp,
    )


class BatchGetDocumentsResponse(proto.Message):
    r"""The streamed response for
    [Firestore.BatchGetDocuments][google.firestore.v1beta1.Firestore.BatchGetDocuments].

    Attributes:
        found (~.gf_document.Document):
            A document that was requested.
        missing (str):
            A document name that was requested but does not exist. In
            the format:
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
        transaction (bytes):
            The transaction that was started as part of this request.
            Will only be set in the first response, and only if
            [BatchGetDocumentsRequest.new_transaction][google.firestore.v1beta1.BatchGetDocumentsRequest.new_transaction]
            was set in the request.
        read_time (~.timestamp.Timestamp):
            The time at which the document was read. This may be
            monotically increasing, in this case the previous documents
            in the result stream are guaranteed not to have changed
            between their read_time and this one.
    """

    found = proto.Field(
        proto.MESSAGE, number=1, oneof="result", message=gf_document.Document,
    )

    missing = proto.Field(proto.STRING, number=2, oneof="result")

    transaction = proto.Field(proto.BYTES, number=3)

    read_time = proto.Field(proto.MESSAGE, number=4, message=timestamp.Timestamp,)


class BeginTransactionRequest(proto.Message):
    r"""The request for
    [Firestore.BeginTransaction][google.firestore.v1beta1.Firestore.BeginTransaction].

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``.
        options (~.common.TransactionOptions):
            The options for the transaction.
            Defaults to a read-write transaction.
    """

    database = proto.Field(proto.STRING, number=1)

    options = proto.Field(proto.MESSAGE, number=2, message=common.TransactionOptions,)


class BeginTransactionResponse(proto.Message):
    r"""The response for
    [Firestore.BeginTransaction][google.firestore.v1beta1.Firestore.BeginTransaction].

    Attributes:
        transaction (bytes):
            The transaction that was started.
    """

    transaction = proto.Field(proto.BYTES, number=1)


class CommitRequest(proto.Message):
    r"""The request for
    [Firestore.Commit][google.firestore.v1beta1.Firestore.Commit].

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``.
        writes (Sequence[~.write.Write]):
            The writes to apply.
            Always executed atomically and in order.
        transaction (bytes):
            If set, applies all writes in this
            transaction, and commits it.
    """

    database = proto.Field(proto.STRING, number=1)

    writes = proto.RepeatedField(proto.MESSAGE, number=2, message=write.Write,)

    transaction = proto.Field(proto.BYTES, number=3)


class CommitResponse(proto.Message):
    r"""The response for
    [Firestore.Commit][google.firestore.v1beta1.Firestore.Commit].

    Attributes:
        write_results (Sequence[~.write.WriteResult]):
            The result of applying the writes.
            This i-th write result corresponds to the i-th
            write in the request.
        commit_time (~.timestamp.Timestamp):
            The time at which the commit occurred.
    """

    write_results = proto.RepeatedField(
        proto.MESSAGE, number=1, message=write.WriteResult,
    )

    commit_time = proto.Field(proto.MESSAGE, number=2, message=timestamp.Timestamp,)


class RollbackRequest(proto.Message):
    r"""The request for
    [Firestore.Rollback][google.firestore.v1beta1.Firestore.Rollback].

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``.
        transaction (bytes):
            Required. The transaction to roll back.
    """

    database = proto.Field(proto.STRING, number=1)

    transaction = proto.Field(proto.BYTES, number=2)


class RunQueryRequest(proto.Message):
    r"""The request for
    [Firestore.RunQuery][google.firestore.v1beta1.Firestore.RunQuery].

    Attributes:
        parent (str):
            Required. The parent resource name. In the format:
            ``projects/{project_id}/databases/{database_id}/documents``
            or
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
            For example:
            ``projects/my-project/databases/my-database/documents`` or
            ``projects/my-project/databases/my-database/documents/chatrooms/my-chatroom``
        structured_query (~.gf_query.StructuredQuery):
            A structured query.
        transaction (bytes):
            Reads documents in a transaction.
        new_transaction (~.common.TransactionOptions):
            Starts a new transaction and reads the
            documents. Defaults to a read-only transaction.
            The new transaction ID will be returned as the
            first response in the stream.
        read_time (~.timestamp.Timestamp):
            Reads documents as they were at the given
            time. This may not be older than 60 seconds.
    """

    parent = proto.Field(proto.STRING, number=1)

    structured_query = proto.Field(
        proto.MESSAGE, number=2, oneof="query_type", message=gf_query.StructuredQuery,
    )

    transaction = proto.Field(proto.BYTES, number=5, oneof="consistency_selector")

    new_transaction = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="consistency_selector",
        message=common.TransactionOptions,
    )

    read_time = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="consistency_selector",
        message=timestamp.Timestamp,
    )


class RunQueryResponse(proto.Message):
    r"""The response for
    [Firestore.RunQuery][google.firestore.v1beta1.Firestore.RunQuery].

    Attributes:
        transaction (bytes):
            The transaction that was started as part of this request.
            Can only be set in the first response, and only if
            [RunQueryRequest.new_transaction][google.firestore.v1beta1.RunQueryRequest.new_transaction]
            was set in the request. If set, no other fields will be set
            in this response.
        document (~.gf_document.Document):
            A query result.
            Not set when reporting partial progress.
        read_time (~.timestamp.Timestamp):
            The time at which the document was read. This may be
            monotonically increasing; in this case, the previous
            documents in the result stream are guaranteed not to have
            changed between their ``read_time`` and this one.

            If the query returns no results, a response with
            ``read_time`` and no ``document`` will be sent, and this
            represents the time at which the query was run.
        skipped_results (int):
            The number of results that have been skipped
            due to an offset between the last response and
            the current response.
    """

    transaction = proto.Field(proto.BYTES, number=2)

    document = proto.Field(proto.MESSAGE, number=1, message=gf_document.Document,)

    read_time = proto.Field(proto.MESSAGE, number=3, message=timestamp.Timestamp,)

    skipped_results = proto.Field(proto.INT32, number=4)


class WriteRequest(proto.Message):
    r"""The request for
    [Firestore.Write][google.firestore.v1beta1.Firestore.Write].

    The first request creates a stream, or resumes an existing one from
    a token.

    When creating a new stream, the server replies with a response
    containing only an ID and a token, to use in the next request.

    When resuming a stream, the server first streams any responses later
    than the given token, then a response containing only an up-to-date
    token, to use in the next request.

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``. This is
            only required in the first message.
        stream_id (str):
            The ID of the write stream to resume.
            This may only be set in the first message. When
            left empty, a new write stream will be created.
        writes (Sequence[~.write.Write]):
            The writes to apply.
            Always executed atomically and in order.
            This must be empty on the first request.
            This may be empty on the last request.
            This must not be empty on all other requests.
        stream_token (bytes):
            A stream token that was previously sent by the server.

            The client should set this field to the token from the most
            recent
            [WriteResponse][google.firestore.v1beta1.WriteResponse] it
            has received. This acknowledges that the client has received
            responses up to this token. After sending this token,
            earlier tokens may not be used anymore.

            The server may close the stream if there are too many
            unacknowledged responses.

            Leave this field unset when creating a new stream. To resume
            a stream at a specific point, set this field and the
            ``stream_id`` field.

            Leave this field unset when creating a new stream.
        labels (Sequence[~.firestore.WriteRequest.LabelsEntry]):
            Labels associated with this write request.
    """

    database = proto.Field(proto.STRING, number=1)

    stream_id = proto.Field(proto.STRING, number=2)

    writes = proto.RepeatedField(proto.MESSAGE, number=3, message=write.Write,)

    stream_token = proto.Field(proto.BYTES, number=4)

    labels = proto.MapField(proto.STRING, proto.STRING, number=5)


class WriteResponse(proto.Message):
    r"""The response for
    [Firestore.Write][google.firestore.v1beta1.Firestore.Write].

    Attributes:
        stream_id (str):
            The ID of the stream.
            Only set on the first message, when a new stream
            was created.
        stream_token (bytes):
            A token that represents the position of this
            response in the stream. This can be used by a
            client to resume the stream at this point.
            This field is always set.
        write_results (Sequence[~.write.WriteResult]):
            The result of applying the writes.
            This i-th write result corresponds to the i-th
            write in the request.
        commit_time (~.timestamp.Timestamp):
            The time at which the commit occurred.
    """

    stream_id = proto.Field(proto.STRING, number=1)

    stream_token = proto.Field(proto.BYTES, number=2)

    write_results = proto.RepeatedField(
        proto.MESSAGE, number=3, message=write.WriteResult,
    )

    commit_time = proto.Field(proto.MESSAGE, number=4, message=timestamp.Timestamp,)


class ListenRequest(proto.Message):
    r"""A request for
    [Firestore.Listen][google.firestore.v1beta1.Firestore.Listen]

    Attributes:
        database (str):
            Required. The database name. In the format:
            ``projects/{project_id}/databases/{database_id}``.
        add_target (~.firestore.Target):
            A target to add to this stream.
        remove_target (int):
            The ID of a target to remove from this
            stream.
        labels (Sequence[~.firestore.ListenRequest.LabelsEntry]):
            Labels associated with this target change.
    """

    database = proto.Field(proto.STRING, number=1)

    add_target = proto.Field(
        proto.MESSAGE, number=2, oneof="target_change", message="Target",
    )

    remove_target = proto.Field(proto.INT32, number=3, oneof="target_change")

    labels = proto.MapField(proto.STRING, proto.STRING, number=4)


class ListenResponse(proto.Message):
    r"""The response for
    [Firestore.Listen][google.firestore.v1beta1.Firestore.Listen].

    Attributes:
        target_change (~.firestore.TargetChange):
            Targets have changed.
        document_change (~.write.DocumentChange):
            A [Document][google.firestore.v1beta1.Document] has changed.
        document_delete (~.write.DocumentDelete):
            A [Document][google.firestore.v1beta1.Document] has been
            deleted.
        document_remove (~.write.DocumentRemove):
            A [Document][google.firestore.v1beta1.Document] has been
            removed from a target (because it is no longer relevant to
            that target).
        filter (~.write.ExistenceFilter):
            A filter to apply to the set of documents
            previously returned for the given target.

            Returned when documents may have been removed
            from the given target, but the exact documents
            are unknown.
    """

    target_change = proto.Field(
        proto.MESSAGE, number=2, oneof="response_type", message="TargetChange",
    )

    document_change = proto.Field(
        proto.MESSAGE, number=3, oneof="response_type", message=write.DocumentChange,
    )

    document_delete = proto.Field(
        proto.MESSAGE, number=4, oneof="response_type", message=write.DocumentDelete,
    )

    document_remove = proto.Field(
        proto.MESSAGE, number=6, oneof="response_type", message=write.DocumentRemove,
    )

    filter = proto.Field(
        proto.MESSAGE, number=5, oneof="response_type", message=write.ExistenceFilter,
    )


class Target(proto.Message):
    r"""A specification of a set of documents to listen to.

    Attributes:
        query (~.firestore.Target.QueryTarget):
            A target specified by a query.
        documents (~.firestore.Target.DocumentsTarget):
            A target specified by a set of document
            names.
        resume_token (bytes):
            A resume token from a prior
            [TargetChange][google.firestore.v1beta1.TargetChange] for an
            identical target.

            Using a resume token with a different target is unsupported
            and may fail.
        read_time (~.timestamp.Timestamp):
            Start listening after a specific ``read_time``.

            The client must know the state of matching documents at this
            time.
        target_id (int):
            The target ID that identifies the target on
            the stream. Must be a positive number and non-
            zero.
        once (bool):
            If the target should be removed once it is
            current and consistent.
    """

    class DocumentsTarget(proto.Message):
        r"""A target specified by a set of documents names.

        Attributes:
            documents (Sequence[str]):
                The names of the documents to retrieve. In the format:
                ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
                The request will fail if any of the document is not a child
                resource of the given ``database``. Duplicate names will be
                elided.
        """

        documents = proto.RepeatedField(proto.STRING, number=2)

    class QueryTarget(proto.Message):
        r"""A target specified by a query.

        Attributes:
            parent (str):
                The parent resource name. In the format:
                ``projects/{project_id}/databases/{database_id}/documents``
                or
                ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
                For example:
                ``projects/my-project/databases/my-database/documents`` or
                ``projects/my-project/databases/my-database/documents/chatrooms/my-chatroom``
            structured_query (~.gf_query.StructuredQuery):
                A structured query.
        """

        parent = proto.Field(proto.STRING, number=1)

        structured_query = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="query_type",
            message=gf_query.StructuredQuery,
        )

    query = proto.Field(
        proto.MESSAGE, number=2, oneof="target_type", message=QueryTarget,
    )

    documents = proto.Field(
        proto.MESSAGE, number=3, oneof="target_type", message=DocumentsTarget,
    )

    resume_token = proto.Field(proto.BYTES, number=4, oneof="resume_type")

    read_time = proto.Field(
        proto.MESSAGE, number=11, oneof="resume_type", message=timestamp.Timestamp,
    )

    target_id = proto.Field(proto.INT32, number=5)

    once = proto.Field(proto.BOOL, number=6)


class TargetChange(proto.Message):
    r"""Targets being watched have changed.

    Attributes:
        target_change_type (~.firestore.TargetChange.TargetChangeType):
            The type of change that occurred.
        target_ids (Sequence[int]):
            The target IDs of targets that have changed.
            If empty, the change applies to all targets.

            The order of the target IDs is not defined.
        cause (~.status.Status):
            The error that resulted in this change, if
            applicable.
        resume_token (bytes):
            A token that can be used to resume the stream for the given
            ``target_ids``, or all targets if ``target_ids`` is empty.

            Not set on every target change.
        read_time (~.timestamp.Timestamp):
            The consistent ``read_time`` for the given ``target_ids``
            (omitted when the target_ids are not at a consistent
            snapshot).

            The stream is guaranteed to send a ``read_time`` with
            ``target_ids`` empty whenever the entire stream reaches a
            new consistent snapshot. ADD, CURRENT, and RESET messages
            are guaranteed to (eventually) result in a new consistent
            snapshot (while NO_CHANGE and REMOVE messages are not).

            For a given stream, ``read_time`` is guaranteed to be
            monotonically increasing.
    """

    class TargetChangeType(proto.Enum):
        r"""The type of change."""
        NO_CHANGE = 0
        ADD = 1
        REMOVE = 2
        CURRENT = 3
        RESET = 4

    target_change_type = proto.Field(proto.ENUM, number=1, enum=TargetChangeType,)

    target_ids = proto.RepeatedField(proto.INT32, number=2)

    cause = proto.Field(proto.MESSAGE, number=3, message=status.Status,)

    resume_token = proto.Field(proto.BYTES, number=4)

    read_time = proto.Field(proto.MESSAGE, number=6, message=timestamp.Timestamp,)


class ListCollectionIdsRequest(proto.Message):
    r"""The request for
    [Firestore.ListCollectionIds][google.firestore.v1beta1.Firestore.ListCollectionIds].

    Attributes:
        parent (str):
            Required. The parent document. In the format:
            ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
            For example:
            ``projects/my-project/databases/my-database/documents/chatrooms/my-chatroom``
        page_size (int):
            The maximum number of results to return.
        page_token (str):
            A page token. Must be a value from
            [ListCollectionIdsResponse][google.firestore.v1beta1.ListCollectionIdsResponse].
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListCollectionIdsResponse(proto.Message):
    r"""The response from
    [Firestore.ListCollectionIds][google.firestore.v1beta1.Firestore.ListCollectionIds].

    Attributes:
        collection_ids (Sequence[str]):
            The collection ids.
        next_page_token (str):
            A page token that may be used to continue the
            list.
    """

    @property
    def raw_page(self):
        return self

    collection_ids = proto.RepeatedField(proto.STRING, number=1)

    next_page_token = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
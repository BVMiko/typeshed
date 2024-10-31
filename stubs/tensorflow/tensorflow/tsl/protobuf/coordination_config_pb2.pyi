"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CoordinatedJob(google.protobuf.message.Message):
    """Represents a job type and the number of tasks under this job.
    For example, ("worker", 20) implies that there will be 20 worker tasks.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUM_TASKS_FIELD_NUMBER: builtins.int
    name: builtins.str
    num_tasks: builtins.int
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        num_tasks: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "num_tasks", b"num_tasks"]) -> None: ...

global___CoordinatedJob = CoordinatedJob

@typing.final
class CoordinationServiceConfig(google.protobuf.message.Message):
    """Coordination service configuration parameters.
    The system picks appropriate values for fields that are not set.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_TYPE_FIELD_NUMBER: builtins.int
    SERVICE_LEADER_FIELD_NUMBER: builtins.int
    ENABLE_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    CLUSTER_REGISTER_TIMEOUT_IN_MS_FIELD_NUMBER: builtins.int
    HEARTBEAT_TIMEOUT_IN_MS_FIELD_NUMBER: builtins.int
    COORDINATED_JOB_LIST_FIELD_NUMBER: builtins.int
    SHUTDOWN_BARRIER_TIMEOUT_IN_MS_FIELD_NUMBER: builtins.int
    AGENT_DESTRUCTION_WITHOUT_SHUTDOWN_FIELD_NUMBER: builtins.int
    RECOVERABLE_JOBS_FIELD_NUMBER: builtins.int
    ALLOW_NEW_INCARNATION_TO_RECONNECT_FIELD_NUMBER: builtins.int
    FORCE_DISABLE_FIELD_NUMBER: builtins.int
    POLL_FOR_ERROR_FROM_SERVICE_AT_STARTUP_FIELD_NUMBER: builtins.int
    service_type: builtins.str
    """Type of coordination service implementation to enable.
    For example, setting the service type as "standalone" starts a service
    instance on the leader task to provide the coordination services such as
    heartbeats and consistent key-value store.
    """
    service_leader: builtins.str
    """Address where the coordination service instance is hosted."""
    enable_health_check: builtins.bool
    """Whether to enable the health check mechanism."""
    cluster_register_timeout_in_ms: builtins.int
    """Maximum wait time for all members in the cluster to be registered."""
    heartbeat_timeout_in_ms: builtins.int
    """Heartbeat timeout, if a task does not record heartbeat in this time
    window, it will be considered disconnected.
    Note: This is also used as a grace period to accept any heartbeats after
    the agent has disconnected, to account for the lag time between the service
    recording the state change and the agent stopping heartbeats.
    """
    shutdown_barrier_timeout_in_ms: builtins.int
    """Denotes how long to wait for all coordination agents to reach the barriers
    (after the first shutdown request) before disconnecting together. If
    set to 0, no barrier is imposed upon shutdown and each worker can
    disconnect individually.
    """
    agent_destruction_without_shutdown: builtins.bool
    """If set, agents do not make an explicit Shutdown() call. Service will only
    find out about the disconnecte agent via stale heartbeats. Used for
    testing.
    """
    allow_new_incarnation_to_reconnect: builtins.bool
    """If a task restarts with a new incarnation, we may allow it to reconnect
    silently. This is useful when we know that a task can immediately resume
    work upon re-connecting to the service.
    """
    force_disable: builtins.bool
    """Disables coordination service.
    Some libraries enable coordination service by default even if the user did
    not specify any config. This field allows users to explicitly disable
    coordination service under all situations.
    """
    poll_for_error_from_service_at_startup: builtins.bool
    """Use long polling to get error from coordination service as the error
    propagation mechanism.
    """
    @property
    def coordinated_job_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CoordinatedJob]: ...
    @property
    def recoverable_jobs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The list of jobs which are recoverable. If a task in this list fails,
        it will not propagate error to other tasks.
        If empty, no jobs will be recoverable and every task failure will cause
        error propagation to other tasks.
        """

    def __init__(
        self,
        *,
        service_type: builtins.str | None = ...,
        service_leader: builtins.str | None = ...,
        enable_health_check: builtins.bool | None = ...,
        cluster_register_timeout_in_ms: builtins.int | None = ...,
        heartbeat_timeout_in_ms: builtins.int | None = ...,
        coordinated_job_list: collections.abc.Iterable[global___CoordinatedJob] | None = ...,
        shutdown_barrier_timeout_in_ms: builtins.int | None = ...,
        agent_destruction_without_shutdown: builtins.bool | None = ...,
        recoverable_jobs: collections.abc.Iterable[builtins.str] | None = ...,
        allow_new_incarnation_to_reconnect: builtins.bool | None = ...,
        force_disable: builtins.bool | None = ...,
        poll_for_error_from_service_at_startup: builtins.bool | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["agent_destruction_without_shutdown", b"agent_destruction_without_shutdown", "allow_new_incarnation_to_reconnect", b"allow_new_incarnation_to_reconnect", "cluster_register_timeout_in_ms", b"cluster_register_timeout_in_ms", "coordinated_job_list", b"coordinated_job_list", "enable_health_check", b"enable_health_check", "force_disable", b"force_disable", "heartbeat_timeout_in_ms", b"heartbeat_timeout_in_ms", "poll_for_error_from_service_at_startup", b"poll_for_error_from_service_at_startup", "recoverable_jobs", b"recoverable_jobs", "service_leader", b"service_leader", "service_type", b"service_type", "shutdown_barrier_timeout_in_ms", b"shutdown_barrier_timeout_in_ms"]) -> None: ...

global___CoordinationServiceConfig = CoordinationServiceConfig

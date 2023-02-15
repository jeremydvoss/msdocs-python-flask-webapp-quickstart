# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from typing import Optional, Sequence

from fixedint import Int32

# pylint:disable=W0611
from opentelemetry.context import Context
from opentelemetry.trace import Link, SpanKind, format_trace_id
from opentelemetry.sdk.trace.sampling import (
    Decision,
    Sampler,
    SamplingResult,
    _get_parent_trace_state,
)
from opentelemetry.trace.span import TraceState
from opentelemetry.util.types import Attributes


_HASH = 5381
_INTEGER_MAX = Int32.maxval
_INTEGER_MIN = Int32.minval


class CustomSampler(Sampler):
    """Sampler that implements the same probability sampling algorithm as the ApplicationInsights SDKs."""

    # sampling_ratio must take a value in the range [0,1]
    def __init__(self, sampling_ratio: float = 1.0):
        if not 0.0 <= sampling_ratio <= 1.0:
            raise ValueError("sampling_ratio must be in the range [0,1]")
        self._ratio = sampling_ratio

    # pylint:disable=C0301
    # See https://github.com/microsoft/Telemetry-Collection-Spec/blob/main/OpenTelemetry/trace/ApplicationInsightsSampler.md
    def should_sample(
        self,
        parent_context: Optional[Context],
        trace_id: int,
        name: str,
        kind: SpanKind = None,
        attributes: Attributes = None,
        links: Sequence["Link"] = None,
        trace_state: "TraceState" = None,
    ) -> "SamplingResult":
        decision = Decision.RECORD_AND_SAMPLE
        return SamplingResult(
            decision,
            attributes,
            _get_parent_trace_state(parent_context),
        )


def azure_monitor_opentelemetry_sampler_factory(sampler_argument):
    try:
        rate = float(sampler_argument)
        return ApplicationInsightsSampler(rate)
    except ValueError:
        return ApplicationInsightsSampler()

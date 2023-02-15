# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, List, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
_MONITOR_OAUTH_SCOPE = "https://monitor.azure.com//.default"
# fmt: off

def build_track_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    credential = kwargs.pop('credential', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/track")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    if credential is not None:
        token = credential.get_token(_MONITOR_OAUTH_SCOPE)
        _header_parameters['Authorization'] = "Bearer {}".format(token.token)
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class AzureMonitorClientOperationsMixin(object):

    def track(
        self,
        body,  # type: List["_models.TelemetryItem"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TrackResponse"
        """Track telemetry events.

        This operation sends a sequence of telemetry events that will be monitored by Azure Monitor.

        :param body: The list of telemetry events to track.
        :type body: list[~azure_monitor_client.models.TelemetryItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TrackResponse, or the result of cls(response)
        :rtype: ~azure_monitor_client.models.TrackResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TrackResponse"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.TrackResponse, response)),
            402: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.TrackResponse, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.TrackResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.TrackResponse, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.TrackResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        credential = kwargs.pop('credential', None)

        _json = self._serialize.body(body, '[TelemetryItem]')

        request = build_track_request(
            content_type=content_type,
            credential=credential,
            json=_json,
            template_url=self.track.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "Host": self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 206]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = self._deserialize('TrackResponse', pipeline_response)

        if response.status_code == 206:
            deserialized = self._deserialize('TrackResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    track.metadata = {'url': "/track"}  # type: ignore


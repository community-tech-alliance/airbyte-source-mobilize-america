#
# MIT License
#
# Copyright (c) 2020 Airbyte
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#use schemas.py to import schema JSONs
from .schemas import organizations_schema, events_schema

import concurrent.futures
import json
import os
from datetime import datetime
from typing import Dict, Generator
from airbyte_cdk.logger import AirbyteLogger
from airbyte_cdk.models import (
    AirbyteCatalog,
    AirbyteConnectionStatus,
    AirbyteMessage,
    AirbyteRecordMessage,
    AirbyteStream,
    ConfiguredAirbyteCatalog,
    Status,
    Type,
)
from airbyte_cdk.sources import Source

from parsons_utilities.mobilize_america import MobilizeAmerica

class SourceMobilizeAmerica(Source):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check(self, logger: AirbyteLogger, config: json) -> AirbyteConnectionStatus:
        """
        Tests if the input configuration can be used to successfully connect to the integration
            e.g: if a provided Stripe API token can be used to connect to the Stripe API.

        :param logger: Logging object to display debug/info/error to the logs
            (logs will not be accessible via airbyte UI if they are not passed to this logger)
        :param config: Json object containing the configuration of this source, content of this json is as specified in
        the properties of the spec.json file

        :return: AirbyteConnectionStatus indicating a Success or Failure
        """

        try:
            updated_since = config['updated_since']
            return AirbyteConnectionStatus(status=Status.SUCCEEDED)
        except Exception as e:
            return AirbyteConnectionStatus(status=Status.FAILED, message=f"An exception occurred: {str(e)}")

    def discover(self, logger: AirbyteLogger, config: json) -> AirbyteCatalog:
        """
        Returns an AirbyteCatalog representing the available streams and fields in this integration.
        For example, given valid credentials to a Postgres database,
        returns an Airbyte catalog where each postgres table is a stream, and each table column is a field.

        :param logger: Logging object to display debug/info/error to the logs
            (logs will not be accessible via airbyte UI if they are not passed to this logger)
        :param config: Json object containing the configuration of this source, content of this json is as specified in
        the properties of the spec.json file

        :return: AirbyteCatalog is an object describing a list of all available streams in this source.
            A stream is an AirbyteStream object that includes:
            - its stream name (or table name in the case of Postgres)
            - json_schema providing the specifications of expected schema for this stream (a list of columns described
            by their names and types)
        """
        streams = []
        streams.append(AirbyteStream(name="organizations", json_schema=organizations_schema))
        streams.append(AirbyteStream(name="organization_events", json_schema=events_schema))

        return AirbyteCatalog(streams=streams)

    def read(
        self, logger: AirbyteLogger, config: json, catalog: ConfiguredAirbyteCatalog, state: Dict[str, any]
    ) -> Generator[AirbyteMessage, None, None]:
        """
        Returns a generator of the AirbyteMessages generated by reading the source with the given configuration,
        catalog, and state.

        :param logger: Logging object to display debug/info/error to the logs
            (logs will not be accessible via airbyte UI if they are not passed to this logger)
        :param config: Json object containing the configuration of this source, content of this json is as specified in
            the properties of the spec.json file
        :param catalog: The input catalog is a ConfiguredAirbyteCatalog which is almost the same as AirbyteCatalog
            returned by discover(), but
        in addition, it's been configured in the UI! For each particular stream and field, there may have been provided
        with extra modifications such as: filtering streams and/or columns out, renaming some entities, etc
        :param state: When a Airbyte reads data from a source, it might need to keep a checkpoint cursor to resume
            replication in the future from that saved checkpoint.
            This is the object that is provided with state from previous runs and avoid replicating the entire set of
            data everytime.

        :return: A generator that produces a stream of AirbyteRecordMessage contained in AirbyteMessage object.
        """
        mob = MobilizeAmerica()

        """
        **********************
        *** /organizations ***
        **********************
        """
        stream_name_organizations = "organizations"
        json_output = mob.get_organizations(updated_since=config['updated_since'],output_format='JSON')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for data in json_output:
                yield AirbyteMessage(
                    type=Type.RECORD,
                    record=AirbyteRecordMessage(
                        stream=stream_name_organizations, data=data,
                        emitted_at=int(datetime.now().timestamp()) * 1000
                    ),
                )

        """
        ***************
        *** /events ***
        ***************
        """
        stream_name_organization_events = "organization_events"

        # OPTIONAL FILTERS:
        # If left blank, set to None
        # TODO(): I'm sure this Python could be more elegant... maybe another day
        try:
            is_virtual = config['is_virtual']
        except:
            is_virtual = None

        try:
            visibility = config['visibility']
        except:
            visibility = None

        try:
            event_types = config['event_types']
        except:
            event_types = None


        events_json = mob.get_organization_events(  organization_id = config['organization_id']
                                                    , updated_since = config['updated_since']
                                                    , timeslot_start = config['timeslot_start']
                                                    , timeslot_end = config['timeslot_end']
                                                    , max_timeslots = config['max_timeslots']
                                                    , zipcode = config['zipcode']
                                                    , max_dist = config['max_dist']
                                                    , visibility = visibility
                                                    , exclude_full = config['exclude_full']
                                                    , is_virtual = is_virtual
                                                    , event_types = 'event_types'
                                                    , api_key = config['Mobilize_API_key']
                                                    , unpack_timeslots = False
                                                    , output_format = 'JSON'
                                                    )

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for data in events_json:
                yield AirbyteMessage(
                    type=Type.RECORD,
                    record=AirbyteRecordMessage(
                        stream=stream_name_organization_events, data=data,
                        emitted_at=int(datetime.now().timestamp()) * 1000
                    ),
                )
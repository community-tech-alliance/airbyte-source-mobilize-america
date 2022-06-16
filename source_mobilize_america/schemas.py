import json

organizations_schema = json.loads(
"""
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "event_feed_url": "https://www.mobilize.us/",
            "state": "CA",
            "is_primary_campaign": false,
            "id": 1,
            "is_independent": false,
            "is_coordinated": false,
            "district": "",
            "name": "Mobilize",
            "org_type": "CAMPAIGN",
            "race_type": null,
            "slug": "mobilize",
            "modified_date": 1630072719,
            "candidate_name": "",
            "created_date": 1511902789
        }
    ],
    "required": [
        "event_feed_url",
        "state",
        "is_primary_campaign",
        "id",
        "is_independent",
        "is_coordinated",
        "district",
        "name",
        "org_type",
        "race_type",
        "slug",
        "modified_date",
        "candidate_name",
        "created_date"
    ],
    "properties": {
        "event_feed_url": {
            "$id": "#/properties/event_feed_url",
            "type": "string",
            "title": "The event_feed_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "https://www.mobilize.us/"
            ]
        },
        "state": {
            "$id": "#/properties/state",
            "type": "string",
            "title": "The state schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "CA"
            ]
        },
        "is_primary_campaign": {
            "$id": "#/properties/is_primary_campaign",
            "type": "boolean",
            "title": "The is_primary_campaign schema",
            "description": "An explanation about the purpose of this instance.",
            "default": false,
            "examples": [
                false
            ]
        },
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "is_independent": {
            "$id": "#/properties/is_independent",
            "type": "boolean",
            "title": "The is_independent schema",
            "description": "An explanation about the purpose of this instance.",
            "default": false,
            "examples": [
                false
            ]
        },
        "is_coordinated": {
            "$id": "#/properties/is_coordinated",
            "type": "boolean",
            "title": "The is_coordinated schema",
            "description": "An explanation about the purpose of this instance.",
            "default": false,
            "examples": [
                false
            ]
        },
        "district": {
            "$id": "#/properties/district",
            "type": "string",
            "title": "The district schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Mobilize"
            ]
        },
        "org_type": {
            "$id": "#/properties/org_type",
            "type": "string",
            "title": "The org_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "CAMPAIGN"
            ]
        },
        "race_type": {
            "$id": "#/properties/race_type",
            "type": "null",
            "title": "The race_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": null,
            "examples": [
                null
            ]
        },
        "slug": {
            "$id": "#/properties/slug",
            "type": "string",
            "title": "The slug schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "mobilize"
            ]
        },
        "modified_date": {
            "$id": "#/properties/modified_date",
            "type": "integer",
            "title": "The modified_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1630072719
            ]
        },
        "candidate_name": {
            "$id": "#/properties/candidate_name",
            "type": "string",
            "title": "The candidate_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "created_date": {
            "$id": "#/properties/created_date",
            "type": "integer",
            "title": "The created_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1511902789
            ]
        }
    },
    "additionalProperties": true
}
"""
)

events_schema = json.loads(
"""
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "created_date": "1611420143",
            "id": "373212",
            "approval_status": "APPROVED",
            "event_type": "COMMUNITY",
            "title": "Pflugerville Area Democrats",
            "is_virtual": "True",
            "visibility": "PUBLIC",
            "tags": "[]",
            "accessibility_notes": "",
            "timeslots": "[{'is_full': False, 'start_date': 1613242800, 'id': 2636893, 'end_date': 1613248200, 'instructions': None}]",
            "browser_url": "https://events.democrats.org/event/373212/",
            "address_visibility": "PUBLIC",
            "accessibility_status": "NOT_SURE",
            "featured_image_url": "https://mobilizeamerica.imgix.net/uploads/event/April2021_Mobilize%20Photo_20210430213116128173.png",
            "high_priority": "False",
            "virtual_action_url": "",
            "instructions": "",
            "description": "stuff",
            "modified_date": "1631477434",
            "event_campaign": "",
            "contact": "",
            "created_by_volunteer_host": "True",
            "summary": "",
            "timezone": "America/Chicago",
            "sponsor_candidate_name": "",
            "sponsor_created_date": "1511902948",
            "sponsor_district": "",
            "sponsor_event_feed_url": "https://events.democrats.org/",
            "sponsor_id": "9",
            "sponsor_is_coordinated": "True",
            "sponsor_is_independent": "False",
            "sponsor_is_primary_campaign": "False",
            "sponsor_modified_date": "1631305611",
            "sponsor_name": "The Democratic National Committee",
            "sponsor_org_type": "PARTY_COMMITTEE",
            "sponsor_race_type": "",
            "sponsor_slug": "dnc",
            "sponsor_state": "",
            "address_lines": " ",
            "congressional_district": "",
            "country": "US",
            "locality": "Pflugerville",
            "postal_code": "78660",
            "region": "TX",
            "state_leg_district": "",
            "state_senate_district": "",
            "venue": "",
            "latitude": "30.4332061",
            "longitude": "-97.6005786"
        }
    ],
    "required": [
        "created_date",
        "id",
        "approval_status",
        "event_type",
        "title",
        "is_virtual",
        "visibility",
        "tags",
        "accessibility_notes",
        "timeslots",
        "browser_url",
        "address_visibility",
        "accessibility_status",
        "featured_image_url",
        "high_priority",
        "virtual_action_url",
        "instructions",
        "description",
        "modified_date",
        "event_campaign",
        "contact",
        "created_by_volunteer_host",
        "summary",
        "timezone",
        "sponsor_candidate_name",
        "sponsor_created_date",
        "sponsor_district",
        "sponsor_event_feed_url",
        "sponsor_id",
        "sponsor_is_coordinated",
        "sponsor_is_independent",
        "sponsor_is_primary_campaign",
        "sponsor_modified_date",
        "sponsor_name",
        "sponsor_org_type",
        "sponsor_race_type",
        "sponsor_slug",
        "sponsor_state",
        "address_lines",
        "congressional_district",
        "country",
        "locality",
        "postal_code",
        "region",
        "state_leg_district",
        "state_senate_district",
        "venue",
        "latitude",
        "longitude"
    ],
    "properties": {
        "created_date": {
            "$id": "#/properties/created_date",
            "type": "string",
            "title": "The created_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1611420143"
            ]
        },
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "373212"
            ]
        },
        "approval_status": {
            "$id": "#/properties/approval_status",
            "type": "string",
            "title": "The approval_status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "APPROVED"
            ]
        },
        "event_type": {
            "$id": "#/properties/event_type",
            "type": "string",
            "title": "The event_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "COMMUNITY"
            ]
        },
        "title": {
            "$id": "#/properties/title",
            "type": "string",
            "title": "The title schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Pflugerville Area Democrats"
            ]
        },
        "is_virtual": {
            "$id": "#/properties/is_virtual",
            "type": "string",
            "title": "The is_virtual schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "True"
            ]
        },
        "visibility": {
            "$id": "#/properties/visibility",
            "type": "string",
            "title": "The visibility schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "PUBLIC"
            ]
        },
        "tags": {
            "$id": "#/properties/tags",
            "type": "string",
            "title": "The tags schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "[]"
            ]
        },
        "accessibility_notes": {
            "$id": "#/properties/accessibility_notes",
            "type": "string",
            "title": "The accessibility_notes schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "timeslots": {
            "$id": "#/properties/timeslots",
            "type": "string",
            "title": "The timeslots schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "[{'is_full': False, 'start_date': 1613242800, 'id': 2636893, 'end_date': 1613248200, 'instructions': None}]"
            ]
        },
        "browser_url": {
            "$id": "#/properties/browser_url",
            "type": "string",
            "title": "The browser_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "https://events.democrats.org/event/373212/"
            ]
        },
        "address_visibility": {
            "$id": "#/properties/address_visibility",
            "type": "string",
            "title": "The address_visibility schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "PUBLIC"
            ]
        },
        "accessibility_status": {
            "$id": "#/properties/accessibility_status",
            "type": "string",
            "title": "The accessibility_status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "NOT_SURE"
            ]
        },
        "featured_image_url": {
            "$id": "#/properties/featured_image_url",
            "type": "string",
            "title": "The featured_image_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "https://mobilizeamerica.imgix.net/uploads/event/April2021_Mobilize%20Photo_20210430213116128173.png"
            ]
        },
        "high_priority": {
            "$id": "#/properties/high_priority",
            "type": "string",
            "title": "The high_priority schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "False"
            ]
        },
        "virtual_action_url": {
            "$id": "#/properties/virtual_action_url",
            "type": "string",
            "title": "The virtual_action_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "instructions": {
            "$id": "#/properties/instructions",
            "type": "string",
            "title": "The instructions schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "description": {
            "$id": "#/properties/description",
            "type": "string",
            "title": "The description schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "stuff"
            ]
        },
        "modified_date": {
            "$id": "#/properties/modified_date",
            "type": "string",
            "title": "The modified_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1631477434"
            ]
        },
        "event_campaign": {
            "$id": "#/properties/event_campaign",
            "type": "string",
            "title": "The event_campaign schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "contact": {
            "$id": "#/properties/contact",
            "type": "string",
            "title": "The contact schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "created_by_volunteer_host": {
            "$id": "#/properties/created_by_volunteer_host",
            "type": "string",
            "title": "The created_by_volunteer_host schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "True"
            ]
        },
        "summary": {
            "$id": "#/properties/summary",
            "type": "string",
            "title": "The summary schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "timezone": {
            "$id": "#/properties/timezone",
            "type": "string",
            "title": "The timezone schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "America/Chicago"
            ]
        },
        "sponsor_candidate_name": {
            "$id": "#/properties/sponsor_candidate_name",
            "type": "string",
            "title": "The sponsor_candidate_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "sponsor_created_date": {
            "$id": "#/properties/sponsor_created_date",
            "type": "string",
            "title": "The sponsor_created_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1511902948"
            ]
        },
        "sponsor_district": {
            "$id": "#/properties/sponsor_district",
            "type": "string",
            "title": "The sponsor_district schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "sponsor_event_feed_url": {
            "$id": "#/properties/sponsor_event_feed_url",
            "type": "string",
            "title": "The sponsor_event_feed_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "https://events.democrats.org/"
            ]
        },
        "sponsor_id": {
            "$id": "#/properties/sponsor_id",
            "type": "string",
            "title": "The sponsor_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "9"
            ]
        },
        "sponsor_is_coordinated": {
            "$id": "#/properties/sponsor_is_coordinated",
            "type": "string",
            "title": "The sponsor_is_coordinated schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "True"
            ]
        },
        "sponsor_is_independent": {
            "$id": "#/properties/sponsor_is_independent",
            "type": "string",
            "title": "The sponsor_is_independent schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "False"
            ]
        },
        "sponsor_is_primary_campaign": {
            "$id": "#/properties/sponsor_is_primary_campaign",
            "type": "string",
            "title": "The sponsor_is_primary_campaign schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "False"
            ]
        },
        "sponsor_modified_date": {
            "$id": "#/properties/sponsor_modified_date",
            "type": "string",
            "title": "The sponsor_modified_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1631305611"
            ]
        },
        "sponsor_name": {
            "$id": "#/properties/sponsor_name",
            "type": "string",
            "title": "The sponsor_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "The Democratic National Committee"
            ]
        },
        "sponsor_org_type": {
            "$id": "#/properties/sponsor_org_type",
            "type": "string",
            "title": "The sponsor_org_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "PARTY_COMMITTEE"
            ]
        },
        "sponsor_race_type": {
            "$id": "#/properties/sponsor_race_type",
            "type": "string",
            "title": "The sponsor_race_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "sponsor_slug": {
            "$id": "#/properties/sponsor_slug",
            "type": "string",
            "title": "The sponsor_slug schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "dnc"
            ]
        },
        "sponsor_state": {
            "$id": "#/properties/sponsor_state",
            "type": "string",
            "title": "The sponsor_state schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "address_lines": {
            "$id": "#/properties/address_lines",
            "type": "string",
            "title": "The address_lines schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                " "
            ]
        },
        "congressional_district": {
            "$id": "#/properties/congressional_district",
            "type": "string",
            "title": "The congressional_district schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "country": {
            "$id": "#/properties/country",
            "type": "string",
            "title": "The country schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "US"
            ]
        },
        "locality": {
            "$id": "#/properties/locality",
            "type": "string",
            "title": "The locality schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Pflugerville"
            ]
        },
        "postal_code": {
            "$id": "#/properties/postal_code",
            "type": "string",
            "title": "The postal_code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "78660"
            ]
        },
        "region": {
            "$id": "#/properties/region",
            "type": "string",
            "title": "The region schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "TX"
            ]
        },
        "state_leg_district": {
            "$id": "#/properties/state_leg_district",
            "type": "string",
            "title": "The state_leg_district schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "state_senate_district": {
            "$id": "#/properties/state_senate_district",
            "type": "string",
            "title": "The state_senate_district schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "venue": {
            "$id": "#/properties/venue",
            "type": "string",
            "title": "The venue schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "latitude": {
            "$id": "#/properties/latitude",
            "type": "string",
            "title": "The latitude schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "30.4332061"
            ]
        },
        "longitude": {
            "$id": "#/properties/longitude",
            "type": "string",
            "title": "The longitude schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "-97.6005786"
            ]
        },
        "organization_id": {
            "$id": "#/properties/organization_id",
            "type": "string",
            "title": "The organization_id",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ]
        }
    },
    "additionalProperties": true
}""")
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from marshmallow import Schema, fields, post_load

from src.schema.base import BaseResponseSchema
from src.model.task import TaskRequest


class RequestSchema(Schema):

    events = fields.Int(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    scheduler = fields.Str(missing="celery")

    @post_load
    def make_task_params(self, data):
        data["datetime_range"] = (data["end_date"] - data['start_date']).total_seconds()
        return TaskRequest(**data)


class TopTenEventsSchema(Schema):
    order = fields.Int(required=True)
    publisher_id = fields.Str(required=True)
    total_events = fields.Int(required=True)


class PublisherStatsSchema(Schema):
    publisher_id = fields.Str(required=True)
    viewable_time = fields.Str(required=True, default="0")
    unique_clips = fields.Int(required=True)


class CountryClipsSchema(Schema):
    country_id = fields.Str(required=True)
    day_clips = fields.Int(required=True)
    night_clips = fields.Int(required=True)


class ResponseSchema(BaseResponseSchema):
    publishers_stats = fields.List(fields.Nested(PublisherStatsSchema))
    top_ten = fields.List(fields.Nested(TopTenEventsSchema))
    clips_per_country = fields.List(fields.Nested(CountryClipsSchema))

# -*- coding: utf-8 -*-

from jsmapper import (
    JSONSchema,
    Mapping,
    object_property,
)
from jsmapper.types import (
    String,
    Object,
)


class Address(Mapping):

    @object_property(name='post-office-box')
    def post_office_box():
        return JSONSchema(type=String())

    @object_property(name='extended-address')
    def extended_address():
        return JSONSchema(type=String())

    @object_property(name='street-address')
    def street_address():
        return JSONSchema(type=String())

    locality = JSONSchema(type=String())
    region = JSONSchema(type=String())

    @object_property(name='postal-code')
    def postal_code():
        return JSONSchema(type=String())

    @object_property(name='country-name')
    def country_name():
        return JSONSchema(type=String())


AddressSchema = JSONSchema(
    type=Object(
        properties=Address,
        dependencies={
            Address.post_office_box: [Address.street_address],
            Address.extended_address: [Address.street_address],
        },
        required=[Address.locality, Address.region],
    ),
    description="An Address following the convention of "
                "http://microformats.org/wiki/hcard",
)

import requests as req
import json as js
from typing import List, Optional
from dataclasses import dataclass
from marshmallow import Schema, fields, post_load

@dataclass
class AddressDTO:
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    street_name: Optional[str] = None
    building_number: Optional[str] = None
    town: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    poi: Optional[bool] = None
    full_address: Optional[str] = None
    google_place_id: Optional[str] = None


@dataclass
class LocationDTO:
    latitude: float = None
    longitude: float = None


@dataclass
class VehicleDTO:
    id: str = None
    type: str = None
    passengers: int = None
    baggages: int = None
    price_variation: float = None
    final_price: float = None


@dataclass
class CancellationRules:
    penalty_amount: int = None
    max_date: Optional[str] = None


@dataclass
class NoShowRules:
    penalty_amount: int = None


@dataclass
class Payment:
    type: str = None
    fare: int = None
    cost: int = None
    breakdown: List[Optional["TaxiFareItem"]] = None


@dataclass
class AssociatedObject:
    id: str = None
    type: str = None


@dataclass
class EphemeralKey:
    id: str = None
    object: str = None
    associated_objects: List[Optional[AssociatedObject]] = None
    created: int = None
    expires: int = None
    livemode: bool = False
    secret: str = None


@dataclass
class StripePaymentData:
    client_secret: str = None
    customer_id: str = None
    ephemeral_key: Optional[EphemeralKey] = None


@dataclass
class TaxiFareItem:
    name: str = None
    cost: int = None


@dataclass
class EstimateResponseDTO:
    estimate_id: str = None
    provider_id: str = None
    provider_code: Optional[str] = None
    provider_name: str = None
    provider_logo: str = None
    eta: Optional[str] = None
    price: float = None
    price_range_min: float = None  # Added field
    price_range_max: float = None  # Added field
    terms_accepted: bool = None
    terms_and_conditions: Optional[str] = None
    cancellation_policies: Optional[str] = None
    pickups: Optional[str] = None
    vehicles: List[VehicleDTO] = None
    verify_phone: bool = None
    passengers: int = None
    vehicle_id: str = None
    vehicle_type: str = None


@dataclass
class TaxiRequestResponseDTO:
    id: str = None
    external_id: str = None
    state: str = None
    ride_status: str = None
    date: Optional[str] = None
    departure: Optional[AddressDTO] = None
    destination: Optional[AddressDTO] = None
    passengers: int = 0
    driver_position: Optional[LocationDTO] = None
    eta: int = 0
    eta_date: Optional[str] = None
    cancellation_reason: Optional[str] = None
    cancellation_rules: Optional[CancellationRules] = None
    noshow_rules: Optional[NoShowRules] = None
    payment: Optional[Payment] = None
    provider_id: str = None
    extra: dict = None
    provider_name: Optional[str] = None
    provider_logo: Optional[str] = None
    client_secret: Optional[str] = None
    arrived_timestamp: int = 0
    receipt_url: Optional[str] = None
    plate: Optional[str] = None
    tag: Optional[str] = None
    phone: Optional[str] = None
    agency: Optional[str] = None
    license: Optional[str] = None
    notes: Optional[str] = None
    stripe_payment_data: Optional[StripePaymentData] = None
    booking_id: Optional[str] = None


@dataclass
class EstimationRequestDTO:
    departure: LocationDTO
    destination: LocationDTO
    date: str
    passengers: int


# Define schemas for the data classes
class AddressDTOSchema(Schema):
    latitude = fields.Float(allow_none=True)
    longitude = fields.Float(allow_none=True)
    street_name = fields.Str(allow_none=True)
    building_number = fields.Str(allow_none=True)
    town = fields.Str(allow_none=True)
    province = fields.Str(allow_none=True)
    country = fields.Str(allow_none=True)
    postal_code = fields.Str(allow_none=True)
    poi = fields.Bool(allow_none=True)
    full_address = fields.Str(allow_none=True)
    google_place_id = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return AddressDTO(**data)


class LocationDTOSchema(Schema):
    latitude = fields.Float(allow_none=True)
    longitude = fields.Float(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return LocationDTO(**data)


class VehicleDTOSchema(Schema):
    id = fields.Str(allow_none=True)
    type = fields.Str(allow_none=True)
    passengers = fields.Int(allow_none=True)
    baggages = fields.Int(allow_none=True)
    price_variation = fields.Float(allow_none=True)
    final_price = fields.Float(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return VehicleDTO(**data)


class CancellationRulesSchema(Schema):
    penalty_amount = fields.Int(allow_none=True)
    max_date = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return CancellationRules(**data)


class NoShowRulesSchema(Schema):
    penalty_amount = fields.Int(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return NoShowRules(**data)


class PaymentSchema(Schema):
    type = fields.Str(allow_none=True)
    fare = fields.Int(allow_none=True)
    cost = fields.Int(allow_none=True)
    breakdown = fields.List(fields.Nested("TaxiFareItemSchema"), allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Payment(**data)


class AssociatedObjectSchema(Schema):
    id = fields.Str(allow_none=True)
    type = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return AssociatedObject(**data)


class EphemeralKeySchema(Schema):
    id = fields.Str(allow_none=True)
    object = fields.Str(allow_none=True)
    associated_objects = fields.List(fields.Nested("AssociatedObjectSchema"), allow_none=True)
    created = fields.Int(allow_none=True)
    expires = fields.Int(allow_none=True)
    livemode = fields.Bool(allow_none=True)
    secret = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return EphemeralKey(**data)


class StripePaymentDataSchema(Schema):
    client_secret = fields.Str(allow_none=True)
    customer_id = fields.Str(allow_none=True)
    ephemeral_key = fields.Nested("EphemeralKeySchema", allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return StripePaymentData(**data)


class TaxiFareItemSchema(Schema):
    name = fields.Str(allow_none=True)
    cost = fields.Int(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return TaxiFareItem(**data)


class EstimateResponseDTOSchema(Schema):
    estimate_id = fields.Str(allow_none=True)
    provider_id = fields.Str(allow_none=True)
    provider_code = fields.Str(allow_none=True)
    provider_name = fields.Str(allow_none=True)
    provider_logo = fields.Str(allow_none=True)
    eta = fields.Str(allow_none=True)
    price = fields.Float(allow_none=True)
    price_range_min = fields.Float(allow_none=True)  # Added field
    price_range_max = fields.Float(allow_none=True)  # Added field
    terms_accepted = fields.Bool(allow_none=True)
    terms_and_conditions = fields.Str(allow_none=True)
    cancellation_policies = fields.Nested(CancellationRulesSchema, allow_none=True)
    pickups = fields.Str(allow_none=True)
    vehicles = fields.List(fields.Nested(VehicleDTOSchema, allow_none=True))
    verify_phone = fields.Bool(allow_none=True)
    passengers = fields.Int(allow_none=True)
    vehicle_id = fields.Str(allow_none=True)
    vehicle_type = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return EstimateResponseDTO(**data)


class TaxiRequestResponseDTOSchema(Schema):
    id = fields.Str(allow_none=True)
    external_id = fields.Str(allow_none=True)
    state = fields.Str(allow_none=True)
    ride_status = fields.Str(allow_none=True)
    date = fields.Str(allow_none=True)
    departure = fields.Nested(AddressDTOSchema, allow_none=True)
    destination = fields.Nested(AddressDTOSchema, allow_none=True)
    passengers = fields.Int(allow_none=True)
    driver_position = fields.Nested(LocationDTOSchema, allow_none=True)
    eta = fields.Int(allow_none=True)
    eta_date = fields.Str(allow_none=True)
    cancellation_reason = fields.Str(allow_none=True)
    cancellation_rules = fields.Nested(CancellationRulesSchema, allow_none=True)
    noshow_rules = fields.Nested(NoShowRulesSchema, allow_none=True)
    payment = fields.Nested(PaymentSchema, allow_none=True)
    provider_id = fields.Str(allow_none=True)
    extra = fields.Dict(allow_none=True)
    provider_name = fields.Str(allow_none=True)
    provider_logo = fields.Str(allow_none=True)
    client_secret = fields.Str(allow_none=True)
    arrived_timestamp = fields.Int(allow_none=True)
    receipt_url = fields.Str(allow_none=True)
    plate = fields.Str(allow_none=True)
    tag = fields.Str(allow_none=True)
    phone = fields.Str(allow_none=True)
    agency = fields.Str(allow_none=True)
    license = fields.Str(allow_none=True)
    notes = fields.Str(allow_none=True)
    stripe_payment_data = fields.Nested(StripePaymentDataSchema, allow_none=True)
    booking_id = fields.Str(allow_none=True)

    @post_load
    def make_object(self, data, **kwargs):
        return TaxiRequestResponseDTO(**data)


class EstimationRequestDTOSchema(Schema):
    departure = fields.Nested(LocationDTOSchema, allow_none=True)
    destination = fields.Nested(LocationDTOSchema, allow_none=True)
    date = fields.Str(allow_none=True)
    passengers = fields.Int(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return EstimateResponseDTO(**data)


@dataclass
class ExtraDTO:
    low_car: bool = False
    pos: bool = None
    bags: int = None


@dataclass
class ReservationRequestDTO:
    vehicle_id: str = None
    passengers: int = None
    departure: AddressDTO = None
    destination: AddressDTO = None
    date: str = None
    estimate_id: str = None
    surname: str = None
    name: str = None
    phone: str = None
    customer_name: str = None
    extra: ExtraDTO = None
    fiscal_code: str = None
    provider_id: str = None
    payment_method: str = None
    payment_in_app: bool = None
    timezone: str = None
    external_id: str = None


class ExtraDTOSchema(Schema):
    low_car = fields.Boolean(allow_none=True)
    pos = fields.Boolean(allow_none=True)
    bags = fields.Integer(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return ExtraDTO(**data)


class ReservationRequestDTOSchema(Schema):
    vehicle_id = fields.Str(allow_none=True)
    passengers = fields.Integer(allow_none=True)
    departure = fields.Nested(AddressDTOSchema, allow_none=True)
    destination = fields.Nested(AddressDTOSchema, allow_none=True)
    date = fields.Str(allow_none=True)
    estimate_id = fields.Str(allow_none=True)
    surname = fields.Str(allow_none=True)
    name = fields.Str(allow_none=True)
    phone = fields.Str(allow_none=True)
    customer_name = fields.Str(allow_none=True)
    extra = fields.Nested(ExtraDTOSchema, allow_none=True)
    fiscal_code = fields.Str(allow_none=True)
    provider_id = fields.Str(allow_none=True)
    payment_method = fields.Str(allow_none=True)
    payment_in_app = fields.Boolean(allow_none=True)
    timezone = fields.Str(allow_none=True)
    external_id = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return ReservationRequestDTO(**data)


@dataclass
class Event:
    event: str = None
    delay: int = None


class EventSchema(Schema):
    event = fields.Str(allow_none=True)
    delay = fields.Int(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Event(**data)


@dataclass
class SimulationRequestDTO:
    procedure: str = None
    departure: AddressDTO = None
    destination: AddressDTO = None
    passengers: int = None
    extra: ExtraDTO = None
    date: Optional[str] = None
    payment_method: str = None
    customer_name: str = None
    fiscal_code: str = None
    timezone: str = None


class SimulationRequestDTOSchema(Schema):
    procedure = fields.Str(required=True)
    departure = fields.Nested(AddressDTOSchema, required=True)
    destination = fields.Nested(AddressDTOSchema, required=True)
    passengers = fields.Int(required=True)
    extra = fields.Nested(ExtraDTOSchema, required=True)
    date = fields.Str(allow_none=True)
    payment_method = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    fiscal_code = fields.Str(required=True)
    timezone = fields.Str(required=True)

    @post_load
    def create(self, data, **kwargs):
        return SimulationRequestDTO(**data)


@dataclass
class CooltraAuthResponseDTO:
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: Optional[int] = None
    scope: Optional[str] = None
    created_at: Optional[int] = None


class CooltraAuthResponseDTOSchema(Schema):
    access_token = fields.Str(required=True)
    token_type = fields.Str(required=True)
    expires_in = fields.Int(required=True)
    scope = fields.Str(required=True)
    created_at = fields.Int(required=True)

    @post_load
    def create(self, data, **kwargs):
        return CooltraAuthResponseDTO(**data)
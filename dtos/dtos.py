from typing import List, Optional
from dataclasses import dataclass
from marshmallow import Schema, fields, post_load
from datetime import datetime


# region DataClasses

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


@dataclass
class CooltraMotoRentalVehicleDTO:
    id: int
    license_plate: str
    position: List[float]
    range: int
    battery_percentage: int
    model_id: int


@dataclass
class CooltraActiveReservationDTO:
    id: str
    provider_id: str
    system_id: str
    created_at: datetime
    expires_at: datetime
    expires_in: int
    vehicle: CooltraMotoRentalVehicleDTO


@dataclass
class CooltraCheckInInfoDTO:
    id: str
    system_id: str
    started_at: datetime
    duration: int
    state: str
    vehicle: CooltraMotoRentalVehicleDTO


@dataclass
class CooltraCheckInRequestDTO:
    qr_code_id: Optional[str] = None
    vehicle_id: Optional[str] = None
    provider_code: str = None



@dataclass
class CooltraCheckoutPolicyDto:
    dismissible_errors: List[str]


@dataclass
class CooltraCheckoutRequestDTO:
    user_id: str
    dismissible: List[str]
    provider_id: str


@dataclass
class CooltraConfigurationResponseDTO:
    systems: List['CooltraSystemDto']
    vehicle_models: Optional[List['CooltraVehicleModelDto']]


@dataclass
class CooltraCurrentActivityResponseDTO:
    reservation: CooltraActiveReservationDTO
    rental: 'CooltraRentalInfoDTO'


@dataclass
class CooltraGeofenceDto:
    type: str
    coordinates: List[List[List[List[float]]]]


@dataclass
class CooltraMotoCoordinates:
    latitude: float
    longitude: float


@dataclass
class CooltraMotoRentalProviderDTO:
    provider_id: str


@dataclass
class CooltraPriceInfo:
    amount: float
    currency: str


@dataclass
class CooltraRentalInfoDTO:
    id: str
    reservation_id: Optional[str]
    duration: int
    billable_duration: int
    prices_include_tax: bool
    price: CooltraPriceInfo
    tax: CooltraPriceInfo
    vehicle: Optional[CooltraMotoRentalVehicleDTO]
    start_point: Optional[CooltraMotoCoordinates]
    end_point: Optional[CooltraMotoCoordinates]
    distance: Optional[int]
    tax_rate: float


@dataclass
class CooltraRentalDTO:
    rental: CooltraRentalInfoDTO


@dataclass
class CooltraReservationCancellationRequestDTO:
    provider_id: str


@dataclass
class CooltraReservationCancellationResultDTO:
    status: int
    body: str


@dataclass
class CooltraReservationInfoDTO:
    id: str
    system_id: str
    created_at: datetime
    expires_at: datetime
    expires_in: int
    vehicle: CooltraMotoRentalVehicleDTO


@dataclass
class CooltraReservationRequestDTO:
    vehicle_id: str
    provider_code: str


@dataclass
class CooltraReservationResultDTO:
    status: int
    body: 'IResponseResult'  # Placeholder for IResponseResult


@dataclass
class CooltraSystemDto:
    id: str
    geofence: CooltraGeofenceDto


@dataclass
class CooltraUserRegistrationRequestDTO:
    external_user_id: str
    first_name: str
    middle_name: str
    last_name: str
    email: str
    phone: str
    language: str
    gender: str
    birthdate: str
    address_street: str
    address_city: str
    address_zip: str
    address_country_code: str
    address_state: str
    provider: str
    provider_code: str


@dataclass
class CooltraUserRegistrationResponseDTO:
    external_id: str
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    phone: str
    language: str
    birthdate: datetime
    address_street: str
    address_city: str
    address_zip: str
    address_state: str
    address_country_code: str
    home_system_id: str
    user_condition: Optional[str]
    email: str
    state: str


@dataclass
class CooltraVehicleActionRequestDTO:
    user_id: str
    action: str
    provider_id: str


@dataclass
class CooltraVehicleActionResultDTO:
    status: int
    body: str


@dataclass
class CooltraVehicleModelDto:
    id: int
    actions: List[str]
    checkout_policy: CooltraCheckoutPolicyDto


@dataclass
class Event:
    event: str = None
    delay: int = None


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


@dataclass
class CooltraAuthResponseDTO:
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: Optional[int] = None
    scope: Optional[str] = None
    created_at: Optional[int] = None


@dataclass
class CooltraTransactionalResponseDTO:
    tid: Optional[str] = None
    status: Optional[str] = None
    finished: Optional[bool] = None
    result: Optional[str] = None


# endregion


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


class EventSchema(Schema):
    event = fields.Str(allow_none=True)
    delay = fields.Int(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Event(**data)


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


class CooltraAuthResponseDTOSchema(Schema):
    access_token = fields.Str(required=True)
    token_type = fields.Str(required=True)
    expires_in = fields.Int(required=True)
    scope = fields.Str(required=True)
    created_at = fields.Int(required=True)

    @post_load
    def create(self, data, **kwargs):
        return CooltraAuthResponseDTO(**data)


from marshmallow import Schema, fields, post_load
from marshmallow_dataclass import class_schema


class CooltraMotoRentalVehicleDTOSchema(Schema):
    id = fields.Int(required=True)
    license_plate = fields.Str(required=False, allow_none=True)
    position = fields.List(fields.Float(), required=True)
    range = fields.Int(required=True)
    battery_percentage = fields.Int(required=True)
    model_id = fields.Int(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraMotoRentalVehicleDTO(**data)


class CooltraActiveReservationDTOSchema(Schema):
    id = fields.Str(required=True)
    system_id = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    expires_at = fields.DateTime(required=True)
    expires_in = fields.Int(required=True)
    vehicle = fields.Nested(CooltraMotoRentalVehicleDTOSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraActiveReservationDTO(**data)


class CooltraCheckInInfoDTOSchema(Schema):
    id = fields.Str(required=True)
    system_id = fields.Str(required=True)
    reservation_id = fields.Str(required=True)
    started_at = fields.DateTime(required=True)
    duration = fields.Int(required=True)
    state = fields.Str(required=True)
    vehicle = fields.Nested(CooltraMotoRentalVehicleDTOSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraCheckInInfoDTO(**data)


class CooltraCheckInRequestDTOSchema(Schema):
    qr_code_id = fields.Str(allow_none=True)
    vehicle_id = fields.Str(allow_none=True)
    provider_code = fields.UUID(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraCheckInRequestDTO(**data)


class CooltraCheckoutPolicyDtoSchema(Schema):
    dismissible_errors = fields.List(fields.Str(), required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraCheckoutPolicyDto(**data)


class CooltraCheckoutRequestDTOSchema(Schema):
    user_id = fields.Str(required=True)
    dismissible = fields.List(fields.Str(), required=True)
    provider_id = fields.UUID(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraCheckoutRequestDTO(**data)


class CooltraConfigurationResponseDTOSchema(Schema):
    systems = fields.List(fields.Nested(lambda: CooltraSystemDtoSchema()), required=True)
    vehicle_models = fields.List(fields.Nested(lambda: CooltraVehicleModelDtoSchema()), required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraConfigurationResponseDTO(**data)


class CooltraCurrentActivityResponseDTOSchema(Schema):
    reservation = fields.Nested(CooltraActiveReservationDTOSchema, required=True)
    rental = fields.Nested(lambda: CooltraRentalInfoDTOSchema(), required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraCurrentActivityResponseDTO(**data)


class CooltraGeofenceDtoSchema(Schema):
    type = fields.Str(required=True)
    coordinates = fields.List(
        fields.List(fields.List(fields.List(fields.Float(), required=True), required=True), required=True),
        required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraGeofenceDto(**data)


class CooltraMotoCoordinatesSchema(Schema):
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraMotoCoordinates(**data)


class CooltraMotoRentalProviderDTOSchema(Schema):
    provider_id = fields.UUID(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraMotoRentalProviderDTO(**data)


class CooltraPriceInfoSchema(Schema):
    amount = fields.Float(required=True)
    currency = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraPriceInfo(**data)


class CooltraRentalInfoDTOSchema(Schema):
    id = fields.Str(required=True)
    reservation_id = fields.Str(allow_none=True)
    duration = fields.Int(required=True)
    billable_duration = fields.Int(required=True)
    prices_include_tax = fields.Bool(required=True)
    price = fields.Nested(CooltraPriceInfoSchema, required=True)
    tax = fields.Nested(CooltraPriceInfoSchema, required=True)
    vehicle = fields.Nested(CooltraMotoRentalVehicleDTOSchema, allow_none=True)
    start_point = fields.Nested(CooltraMotoCoordinatesSchema, allow_none=True)
    end_point = fields.Nested(CooltraMotoCoordinatesSchema, allow_none=True)
    distance = fields.Int(allow_none=True)
    tax_rate = fields.Float(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraRentalInfoDTO(**data)


class CooltraRentalDTOSchema(Schema):
    rental = fields.Nested(CooltraRentalInfoDTOSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraRentalDTO(**data)


class CooltraReservationCancellationRequestDTOSchema(Schema):
    provider_id = fields.UUID(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraReservationCancellationRequestDTO(**data)


class CooltraReservationCancellationResultDTOSchema(Schema):
    status = fields.Int(required=True)
    body = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraReservationCancellationResultDTO(**data)


class CooltraReservationInfoDTOSchema(Schema):
    id = fields.Str(required=True)
    system_id = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    expires_at = fields.DateTime(required=True)
    expires_in = fields.Int(required=True)
    vehicle = fields.Nested(CooltraMotoRentalVehicleDTOSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraReservationInfoDTO(**data)


class CooltraReservationRequestDTOSchema(Schema):
    vehicle_id = fields.Str(required=True)
    provider_code = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraReservationRequestDTO(**data)


class CooltraReservationResultDTOSchema(Schema):
    status = fields.Int(required=True)
    body = fields.Raw(required=True)  # Generic field to handle any type

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraReservationResultDTO(**data)


class CooltraSystemDtoSchema(Schema):
    id = fields.Str(required=True)
    geofence = fields.Nested(CooltraGeofenceDtoSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraSystemDto(**data)


class CooltraUserRegistrationRequestDTOSchema(Schema):
    external_user_id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    language = fields.Str(required=True)
    gender = fields.Str(required=True)
    birthdate = fields.Str(required=True)
    address_street = fields.Str(required=True)
    address_city = fields.Str(required=True)
    address_zip = fields.Str(required=True)
    address_country_code = fields.Str(required=True)
    address_state = fields.Str(required=True)
    provider = fields.Str(required=True)
    provider_code = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraUserRegistrationRequestDTO(**data)


class CooltraUserRegistrationResponseDTOSchema(Schema):
    external_id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    gender = fields.Str(required=True)
    phone = fields.Str(required=True)
    language = fields.Str(required=True)
    birthdate = fields.DateTime(required=True)
    address_street = fields.Str(required=True)
    address_city = fields.Str(required=True)
    address_zip = fields.Str(required=True)
    address_state = fields.Str(required=True)
    address_country_code = fields.Str(required=True)
    home_system_id = fields.Str(required=True)
    user_condition = fields.Str(allow_none=True)
    email = fields.Str(required=True)
    state = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraUserRegistrationResponseDTO(**data)


class CooltraVehicleActionRequestDTOSchema(Schema):
    user_id = fields.Str(required=True)
    action = fields.Str(required=True)
    provider_id = fields.UUID(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraVehicleActionRequestDTO(**data)


class CooltraVehicleActionResultDTOSchema(Schema):
    status = fields.Int(required=True)
    body = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraVehicleActionResultDTO(**data)


class CooltraVehicleModelDtoSchema(Schema):
    id = fields.Int(required=True)
    actions = fields.List(fields.Str(), required=True)
    checkout_policy = fields.Nested(CooltraCheckoutPolicyDtoSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraVehicleModelDto(**data)


class CooltraTransactionalResponseDTOSchema(Schema):
    tid = fields.Str(required=True, allow_none=True)
    status = fields.Str(required=True, allow_none=True)
    finished = fields.Bool(required=True, allow_none=True)
    result = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return CooltraTransactionalResponseDTO(**data)


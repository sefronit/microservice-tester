from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from marshmallow import Schema, fields, post_load


@dataclass
class TwoWheelsAnyEmployeeDto:
    has_any_employee: bool


class TwoWheelsAnyEmployeeDtoSchema(Schema):
    has_any_employee = fields.Bool(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsAnyEmployeeDto(**data)


@dataclass
class TwoWheelsEmployeeDto:
    id: str
    client_id: str
    language: str


class TwoWheelsEmployeeDtoSchema(Schema):
    id = fields.Str(required=True, allow_none=True)
    client_id = fields.Str(required=True, allow_none=True)
    language = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsEmployeeDto(**data)


@dataclass
class TwoWheelsEmployeeCreateInputDto:
    id: str
    client_id: str


class TwoWheelsEmployeeCreateInputDtoSchema(Schema):
    id = fields.Str(required=True, allow_none=True)
    client_id = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsEmployeeCreateInputDto(**data)


@dataclass
class TwoWheelsEmployeeUpdateInputDto:
    client_id: str
    language: str


class TwoWheelsEmployeeUpdateInputDtoSchema(Schema):
    client_id = fields.Str(required=True, allow_none=True)
    language = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsEmployeeUpdateInputDto(**data)


@dataclass
class TwoWheelsEmployeeCreateExampleInputDto:
    number: int
    client_id: str


class TwoWheelsEmployeeCreateExampleInputDtoSchema(Schema):
    number = fields.Int(required=True)
    client_id = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsEmployeeCreateExampleInputDto(**data)


@dataclass
class TwoWheelsEmployeeDtoPaginatedResultDto:
    elements: list[TwoWheelsEmployeeDto]
    page_index: int
    page_size: int
    total_count: int
    total_pages: int
    has_previous_page: bool
    has_next_page: bool


class TwoWheelsEmployeeDtoPaginatedResultDtoSchema(Schema):
    elements = fields.List(fields.Nested(TwoWheelsEmployeeDtoSchema), required=True, allow_none=True)
    page_index = fields.Int(required=True, allow_none=True)
    page_size = fields.Int(required=True, allow_none=True)
    total_count = fields.Int(required=True, allow_none=True)
    total_pages = fields.Int(required=True, allow_none=True)
    has_previous_page = fields.Bool(required=True)
    has_next_page = fields.Bool(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsEmployeeDtoPaginatedResultDto(**data)


@dataclass
class TwoWheelsErrorResponse:
    errors: list[str]
    code: str
    module: str


class TwoWheelsErrorResponseSchema(Schema):
    errors = fields.List(fields.Str(), required=True)
    code = fields.Str(required=True)
    module = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsErrorResponse(**data)


@dataclass
class TwoWheelsReservationRequestDTO:
    vehicle_id: int
    provider_code: str


class TwoWheelsReservationRequestDTOSchema(Schema):
    vehicle_id = fields.Int(required=True)
    provider_code = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsReservationRequestDTO(**data)


@dataclass
class TwoWheelsReservationCancellationRequestDTO:
    user_id: str
    provider_code: str


class TwoWheelsReservationCancellationRequestDTOSchema(Schema):
    user_id = fields.Str(required=True, allow_none=True)
    provider_code = fields.Str(required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsReservationCancellationRequestDTO(**data)


@dataclass
class TwoWheelsTripCreationRequestDTO:
    vehicle_id: str
    idempotency_key: str
    provider_code: str
    start_location_lat: float
    start_location_lon: float


class TwoWheelsTripCreationRequestDTOSchema(Schema):
    vehicle_id = fields.Str(required=True, allow_none=True)
    idempotency_key = fields.Str(required=True)
    provider_code = fields.Str(required=True, allow_none=True)
    start_location_lat = fields.Float(required=True)
    start_location_lon = fields.Float(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsTripCreationRequestDTO(**data)


@dataclass
class TwoWheelsTripEndRequestDTO:
    idempotency_key: str
    end_location: dict
    dismiss: list[str]


class TwoWheelsTripEndRequestDTOSchema(Schema):
    idempotency_key = fields.Str(required=True)
    end_location = fields.Nested('LocationDTOSchema', required=True, allow_none=True)
    dismiss = fields.List(fields.Str(), required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsTripEndRequestDTO(**data)


@dataclass
class TwoWheelsAllProvidersDTO:
    providers: list[str]


class TwoWheelsAllProvidersDTOSchema(Schema):
    providers = fields.List(fields.Str(), required=True, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsAllProvidersDTO(**data)


@dataclass
class TwoWheelsVehicleSearchFilters:
    north_east_lat: float = None
    north_east_lon: float = None
    south_west_lat: float = None
    south_west_lon: float = None
    vehicle_types: List[str] = None
    provider_codes: List[str] = None
    battery_level_ranges: List[str] = None
    system_id: str = None


class TwoWheelsVehicleSearchFiltersSchema(Schema):
    north_east_lat = fields.Float(required=False, allow_none=True)
    north_east_lon = fields.Float(required=False, allow_none=True)
    south_west_lat = fields.Float(required=False, allow_none=True)
    south_west_lon = fields.Float(required=False, allow_none=True)
    vehicle_types = fields.List(fields.Str(), required=False, allow_none=True)
    provider_codes: fields.List(fields.Str(), required=False, allow_none=True)
    battery_level_ranges: fields.List(fields.Str(), required=False, allow_none=True)
    system_id = fields.Str(required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehicleSearchFilters(**data)


@dataclass
class TwoWheelsVehicleModelDTO:
    id: int
    actions: Optional[List[str]]
    checkout_policy: Optional[dict]


@dataclass
class PriceInfoDTO:
    value: float
    currency: str


class PriceInfoDTOSchema(Schema):
    value = fields.Float(required=True)
    currency = fields.Str(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return PriceInfoDTO(**data)


@dataclass
class VehicleChargeDTO:
    riding: PriceInfoDTO
    pausing: PriceInfoDTO
    starting: PriceInfoDTO


class VehicleChargeDTOSchema(Schema):
    riding = fields.Nested(PriceInfoDTOSchema, required=True)
    pausing = fields.Nested(PriceInfoDTOSchema, required=True)
    starting = fields.Nested(PriceInfoDTOSchema, required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return VehicleChargeDTO(**data)


@dataclass
class SubscriptionChargeDTO:
    scooter: VehicleChargeDTO = None
    bicycle: VehicleChargeDTO = None


class SubscriptionChargeDTOSchema(Schema):
    scooter = fields.Nested(VehicleChargeDTOSchema, required=False, allow_none=True)
    bicycle = fields.Nested(VehicleChargeDTOSchema, required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return SubscriptionChargeDTO(**data)


@dataclass
class TwoWheelsSystemDTO:
    id: str
    geofence: dict
    charges: SubscriptionChargeDTO


class TwoWheelsSystemDTOSchema(Schema):
    id = fields.Str(required=True)
    geofence = fields.Dict(required=True)
    charges = fields.Nested(SubscriptionChargeDTOSchema, required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsSystemDTO(**data)


@dataclass
class TwoWheelsConfigurationResponseDTO:
    systems: Optional[List[TwoWheelsSystemDTO]]
    vehicle_models: Optional[List[TwoWheelsVehicleModelDTO]]


class TwoWheelsVehicleModelDTOSchema(Schema):
    id = fields.Int(required=True)
    actions = fields.List(fields.Str(), required=False, allow_none=True)
    checkout_policy = fields.Dict(required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehicleModelDTO(**data)


class TwoWheelsConfigurationResponseDTOSchema(Schema):
    systems = fields.List(fields.Nested(TwoWheelsSystemDTOSchema), required=False, allow_none=True)
    vehicle_models = fields.List(fields.Nested(TwoWheelsVehicleModelDTOSchema), required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsConfigurationResponseDTO(**data)


@dataclass
class TwoWheelsVehiclePricingDTO:
    rate: float = None
    start: int = None
    end: int = None
    interval: int = None


class TwoWheelsVehiclePricingDTOSchema(Schema):
    rate = fields.Float(required=False, allow_none=True)
    start = fields.Int(required=False, allow_none=True)
    end = fields.Int(required=False, allow_none=True)
    interval = fields.Int(required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehiclePricingDTO(**data)


@dataclass
class TwoWheelsVehicleDTO:
    id: str = None
    battery_level: int = None
    battery_level_range: str = None
    available_range: int = None
    vehicle_type: str = None
    provider_vehicle_type_id: str = None
    propulsion: str = None
    lat: float = None
    lon: float = None
    provider_logo_url: str = None
    provider_name: str = None
    provider_code: str = None
    provider_id: UUID = None
    verify_age: bool = None
    verify_driving_license: bool = None
    can_scan: bool = None
    can_ring: bool = None
    start_price: float = None
    ride_price: float = None
    pause_price: float = None
    per_minute_pricing: List[TwoWheelsVehiclePricingDTO] = None
    per_km_pricing: List[TwoWheelsVehiclePricingDTO] = None
    pricing_plan_id: str = None
    license_plate: str = None
    system_id: str = None
    model_id: str = None


class TwoWheelsVehicleDTOSchema(Schema):
    id = fields.Str(required=False, allow_none=True)
    battery_level = fields.Int(required=False, allow_none=True)
    battery_level_range = fields.Str(required=False, allow_none=True)
    available_range = fields.Int(required=False, allow_none=True)
    vehicle_type = fields.Str(required=False, allow_none=True)
    provider_vehicle_type_id = fields.Str(required=False, allow_none=True)
    propulsion = fields.Str(required=False, allow_none=True)
    lat = fields.Float(required=False, allow_none=True)
    lon = fields.Float(required=False, allow_none=True)
    provider_logo_url = fields.Str(required=False, allow_none=True)
    provider_name = fields.Str(required=False, allow_none=True)
    provider_code = fields.Str(required=False, allow_none=True)
    provider_id = fields.UUID(required=False, allow_none=True)
    verify_age = fields.Bool(required=False, allow_none=True)
    verify_driving_license = fields.Bool(required=False, allow_none=True)
    can_scan = fields.Bool(required=False, allow_none=True)
    can_ring = fields.Bool(required=False, allow_none=True)
    start_price = fields.Float(required=False, allow_none=True)
    ride_price = fields.Float(required=False, allow_none=True)
    pause_price = fields.Float(required=False, allow_none=True)
    per_minute_pricing = fields.List(fields.Nested(TwoWheelsVehiclePricingDTOSchema), required=False, allow_none=True)
    per_km_pricing = fields.List(fields.Nested(TwoWheelsVehiclePricingDTOSchema), required=False, allow_none=True)
    pricing_plan_id = fields.Str(required=False, allow_none=True)
    license_plate = fields.Str(required=False, allow_none=True)
    system_id = fields.Str(required=False, allow_none=True)
    model_id = fields.Str(required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehicleDTO(**data)


@dataclass
class TwoWheelsVehiclesDTO:
    vehicles: Optional[List[TwoWheelsVehicleDTO]]


class TwoWheelsVehiclesDTOSchema(Schema):
    vehicles = fields.List(fields.Nested(TwoWheelsVehicleDTOSchema), required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehiclesDTO(**data)

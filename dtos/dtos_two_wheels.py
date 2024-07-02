from dataclasses import dataclass
from typing import List, Optional

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
    user_id: str
    vehicle_id: int
    provider_code: str


class TwoWheelsReservationRequestDTOSchema(Schema):
    user_id = fields.Str(required=True, allow_none=True)
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
class TwoWheelsSystemDTO:
    id: str
    geofence: dict


@dataclass
class TwoWheelsVehicleModelDTO:
    id: int
    actions: Optional[List[str]]
    checkout_policy: Optional[dict]


@dataclass
class TwoWheelsConfigurationResponseDTO:
    systems: Optional[List[TwoWheelsSystemDTO]]
    vehicle_models: Optional[List[TwoWheelsVehicleModelDTO]]


class TwoWheelsSystemDTOSchema(Schema):
    id = fields.Str(required=True)
    geofence = fields.Dict(required=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsSystemDTO(**data)


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
class TwoWheelsVehiclesDTO:
    vehicles: Optional[List[TwoWheelsVehicleModelDTO]]


class TwoWheelsVehiclesDTOSchema(Schema):
    vehicles = fields.List(fields.Nested(TwoWheelsVehicleModelDTO), required=False, allow_none=True)

    @post_load
    def make_instance(self, data, **kwargs):
        return TwoWheelsVehiclesDTO(**data)
